import json
from pathlib import Path

import pytest

from homedesign.compiler import compile_spec
from homedesign import pdf
from homedesign.plan2d import write_plans

REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = REPO_ROOT / "spec" / "examples"


def load_example(name):
    return json.loads((EXAMPLES / name).read_text())


@pytest.fixture(scope="module")
def drawn_out(tmp_path_factory):
    """Fresh plans/elevations/sections for tubehouse-mini in a temp output dir;
    `output/` is gitignored, so CI has no pre-built drawings."""
    out = tmp_path_factory.mktemp("output")
    write_plans(compile_spec(load_example("tubehouse-mini.json")), out)
    return out


def _brief():
    return {
        "title": "Test House Brief",
        "subtitle": "A design-intent brief",
        "narrative": ["Paragraph one.", "Paragraph two."],
        "requirements": ["Requirement A", "Requirement B"],
    }


def test_print_html_to_pdf_passes_an_absolute_path(tmp_path, monkeypatch):
    """Headless Chromium resolves --print-to-pdf against its own working
    directory, not the caller's, so a relative path silently fails
    (regression: contractor-as-drawn-brief.pdf stayed 4 days stale while
    every `homedesign pdf` run reported success)."""
    html_path = tmp_path / "brief.html"
    html_path.write_text("<html></html>", encoding="utf-8")
    pdf_path = Path("relative/out.pdf")  # deliberately not absolute
    captured = {}

    def fake_run(cmd, capture_output, text):
        captured["cmd"] = cmd
        (tmp_path / "sentinel").touch()  # proves the fake ran
        Path(cmd[3].split("=", 1)[1]).parent.mkdir(parents=True, exist_ok=True)
        Path(cmd[3].split("=", 1)[1]).write_bytes(b"%PDF-1.4 fake")
        return type("R", (), {"returncode": 0, "stderr": ""})()

    monkeypatch.setattr(pdf.subprocess, "run", fake_run)
    monkeypatch.setattr(pdf, "_find_browser", lambda: "fake-browser")
    monkeypatch.chdir(tmp_path)
    pdf.print_html_to_pdf(html_path, pdf_path)
    printed_arg = captured["cmd"][3]
    assert printed_arg.startswith("--print-to-pdf=")
    assert Path(printed_arg.split("=", 1)[1]).is_absolute()


def test_print_html_to_pdf_raises_when_output_is_stale(tmp_path, monkeypatch):
    """A browser that exits 0 but never touches the output (the exact
    EdgeCore/Chromium failure mode this regression hit) must raise, not
    silently leave a pre-existing PDF in place."""
    html_path = tmp_path / "brief.html"
    html_path.write_text("<html></html>", encoding="utf-8")
    pdf_path = tmp_path / "out.pdf"
    pdf_path.write_bytes(b"%PDF-1.4 stale")
    stale_mtime = pdf_path.stat().st_mtime

    def fake_run_noop(cmd, capture_output, text):
        return type("R", (), {"returncode": 0, "stderr": "cannot find the path specified"})()

    monkeypatch.setattr(pdf.subprocess, "run", fake_run_noop)
    monkeypatch.setattr(pdf, "_find_browser", lambda: "fake-browser")
    with pytest.raises(RuntimeError, match="PDF print failed"):
        pdf.print_html_to_pdf(html_path, pdf_path)
    assert pdf_path.stat().st_mtime == stale_mtime


def test_room_schedule_lists_every_room_with_area_and_floor_totals():
    model = compile_spec(load_example("tubehouse-mini.json"))
    schedule = pdf.build_room_schedule(model)
    assert len(schedule) == len(model.storeys)
    ground = schedule[0]
    assert {r["id"] for r in ground["rooms"]} == {"living", "stairwell", "hall", "bedroom"}
    living = next(r for r in ground["rooms"] if r["id"] == "living")
    assert living["area_m2"] == 20.0  # 4m x 5m
    assert ground["total_m2"] == sum(r["area_m2"] for r in ground["rooms"])


def test_render_brief_html_includes_title_narrative_and_requirements(drawn_out):
    model = compile_spec(load_example("tubehouse-mini.json"))
    html = pdf.render_brief_html(model, _brief(), drawn_out, REPO_ROOT / "spec" / "examples" / "tubehouse-mini.json")
    assert "Test House Brief" in html
    assert "Paragraph one." in html
    assert "Requirement A" in html
    assert "@page { size: A3 landscape;" in html


def test_render_brief_html_includes_one_plan_page_per_storey(drawn_out):
    model = compile_spec(load_example("tubehouse-mini.json"))
    html = pdf.render_brief_html(model, _brief(), drawn_out, REPO_ROOT / "spec" / "examples" / "tubehouse-mini.json")
    for storey in model.storeys:
        assert storey.name in html


def test_render_brief_html_lists_handover_files(drawn_out):
    model = compile_spec(load_example("tubehouse-mini.json"))
    spec_path = REPO_ROOT / "spec" / "examples" / "tubehouse-mini.json"
    html = pdf.render_brief_html(model, _brief(), drawn_out, spec_path)
    assert spec_path.name in html
    assert "tubehouse-mini_f0.dxf" in html


def test_gallery_pages_batches_two_images_per_page(tmp_path):
    imgs = []
    for i in range(3):
        p = tmp_path / f"img{i}.png"
        p.write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 20)
        imgs.append(p)
    html = pdf._gallery_pages(imgs, embed_images=True, img_dir=tmp_path)
    assert html.count('class="page"') == 2  # 3 images at 2/page -> 2 pages


def test_opening_schedule_covers_all_openings():
    model = compile_spec(load_example("tubehouse-mini.json"))
    rows = pdf.build_opening_schedule(model)
    total_openings = sum(len(s.openings) for s in model.storeys)
    assert len(rows) == total_openings
    assert all(len(r["rooms"]) == 2 for r in rows)


def test_takeoff_totals_row_matches_sum():
    model = compile_spec(load_example("tubehouse-mini.json"))
    rows = pdf.build_takeoff(model)
    # Final row is Total; the row before it is the built-envelope disclosure.
    assert rows[-1]["level"] is None
    assert rows[-2]["name"].startswith("Built envelope")
    per_storey = sum(r["gfa_m2"] for r in rows[:-2])
    assert abs(rows[-1]["gfa_m2"] - per_storey) < 0.1


def test_render_brief_html_uses_relative_images_not_data_uris(drawn_out):
    model = compile_spec(load_example("tubehouse-mini.json"))
    out = drawn_out
    _write_renders(out, model)
    html = pdf.render_brief_html(model, _brief(), out, EXAMPLES / "tubehouse-mini.json")
    # Gallery images referenced by relative path; the single cover-hero data
    # URI is the only base64 occurrence allowed.
    assert html.count("data:image/png;base64") == 1
    assert 'src="../pdf/img/' in html


def test_render_brief_html_embed_images_embeds_all(drawn_out):
    model = compile_spec(load_example("tubehouse-mini.json"))
    out = drawn_out
    _write_renders(out, model)
    html = pdf.render_brief_html(model, _brief(), out, EXAMPLES / "tubehouse-mini.json",
                                 embed_images=True)
    n_views = len(model.views) or 2
    assert html.count("data:image/png;base64") == n_views + 1  # gallery + hero


def test_render_brief_html_includes_elevation_and_section_pages(drawn_out):
    model = compile_spec(load_example("tubehouse-mini.json"))
    html = pdf.render_brief_html(model, _brief(), drawn_out,
                                 EXAMPLES / "tubehouse-mini.json")
    for heading in ("North Elevation", "South Elevation", "East Elevation", "West Elevation",
                    "Long Section", "Cross Section"):
        assert heading in html


def _write_real_png(path):
    try:
        from PIL import Image
    except ImportError:
        pytest.skip("Pillow unavailable")
    Image.new("RGB", (12, 12), (255, 0, 0)).save(path)


def _write_renders(out, model):
    """Tiny real PNGs for every view, so the gallery has images to embed."""
    png_dir = out / "png"
    png_dir.mkdir(exist_ok=True)
    for view in [v.name for v in model.views] or ["exterior", "interior"]:
        _write_real_png(png_dir / f"{model.name}_{view}.png")


def _stale_setup(tmp_path, hashes):
    """One real PNG per hash with a matching render sidecar; returns paths."""
    from homedesign.model import write_render_sidecar

    paths = []
    for i, h in enumerate(hashes):
        p = tmp_path / f"img{i}.png"
        _write_real_png(p)
        write_render_sidecar(p, h, f"view{i}", "final")
        paths.append(p)
    return paths


def test_gallery_stale_badge_is_per_image_on_mixed_page(tmp_path):
    stale, fresh = _stale_setup(tmp_path, ["999999", "abc123"])
    html = pdf._gallery_pages([stale, fresh], embed_images=False, img_dir=tmp_path, current_hash="abc123")
    assert html.count(">STALE<") == 1
    # The single badge sits inside the same <figure> as the stale image.
    figure = html[html.index("<figure>"): html.index("</figure>") + len("</figure>")]
    assert stale.name in figure
    assert ">STALE<" in figure


def test_gallery_stale_badge_counts_every_stale_image(tmp_path):
    a, b = _stale_setup(tmp_path, ["999999", "999999"])
    html = pdf._gallery_pages([a, b], embed_images=False, img_dir=tmp_path, current_hash="abc123")
    assert html.count(">STALE<") == 2


def test_gallery_stale_badge_absent_when_all_fresh(tmp_path):
    a, b = _stale_setup(tmp_path, ["abc123", "abc123"])
    html = pdf._gallery_pages([a, b], embed_images=False, img_dir=tmp_path, current_hash="abc123")
    assert ">STALE<" not in html


def test_render_brief_html_escapes_brief_title(drawn_out):
    model = compile_spec(load_example("tubehouse-mini.json"))
    brief = _brief()
    brief["title"] = "Nhà & Sân"
    html = pdf.render_brief_html(model, brief, drawn_out,
                                 EXAMPLES / "tubehouse-mini.json")
    assert "Nhà &amp; Sân" in html
    assert "Nhà & Sân" not in html
    assert "<svg" in html
