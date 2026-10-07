await page.setViewportSize({ width: 375, height: 812 });
await page.goto("http://localhost:8765/tmp_viewer.html", { waitUntil: "domcontentloaded" });
await page.waitForTimeout(8000);
await page.waitForFunction(() => document.getElementById('overlay')?.classList.contains('hidden'), null, { timeout: 15000 }).catch(()=>{});
await page.waitForTimeout(1000);
const out = "C:/Users/tukum/Downloads/freecad-blender/tmp/critic-375x812.png";
await page.screenshot({ path: out, timeout: 15000 });
return { ok: true, out };
