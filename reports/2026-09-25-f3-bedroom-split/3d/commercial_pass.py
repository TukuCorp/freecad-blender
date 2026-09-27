"""Commercial-quality render pass for the F3 split viewer (visual only)."""
from pathlib import Path
HERE = Path(__file__).resolve().parent
TPL = HERE / "viewer_page_template.html"
t = TPL.read_text(encoding="utf-8")
def sub(old, new):
    global t
    n = t.count(old)
    assert n == 1, "anchor x%d: %r" % (n, old[:70])
    t = t.replace(old, new)
def rep_between(start, end, new):
    global t
    i = t.index(start)
    j = t.index(end, i)
    assert i < j
    t = t[:i] + new + t[j:]
sub("  renderer.shadowMap.enabled = true;",
    "  renderer.outputEncoding = THREE.sRGBEncoding;\n"
    "  renderer.toneMapping = THREE.ACESFilmicToneMapping;\n"
    "  renderer.toneMappingExposure = 1.12;\n"
    "  renderer.shadowMap.enabled = true;")
sub("  scene.background = new THREE.Color(0x23262e);\n"
    "  scene.add(new THREE.HemisphereLight(0xffffff, 0x4a505c, 1.25));\n"
    "  var sun = new THREE.DirectionalLight(0xffffff, 0.85);",
    "  scene.background = new THREE.Color(0xdcd9d2);\n"
    "  scene.fog = new THREE.Fog(0xdcd9d2, 38, 110);\n"
    "  scene.add(new THREE.HemisphereLight(0xfff6ea, 0x8a8d94, 0.85));\n"
    "  var sun = new THREE.DirectionalLight(0xfff1dd, 1.05);")
sub("  sun.shadow.bias = -0.0005;",
    "  sun.shadow.bias = -0.0004;")
sub("  var fill = new THREE.DirectionalLight(0xfff2e0, 0.30);\n"
    "  fill.position.set(-6, 8, -14);\n"
    "  scene.add(fill);",
    "  var fill = new THREE.DirectionalLight(0xe8f0ff, 0.35);\n"
    "  fill.position.set(-6, 8, -14);\n"
    "  scene.add(fill);\n"
    "  var bounce = new THREE.DirectionalLight(0xffffff, 0.18);\n"
    "  bounce.position.set(2, 4, -6);\n"
    "  scene.add(bounce);\n"
    "  var glowA = new THREE.PointLight(0xffd9a8, 0.55, 7, 2);\n"
    "  glowA.position.set(1.98, 5.6, 2.6);\n"
    "  scene.add(glowA);\n"
    "  var glowB = new THREE.PointLight(0xffe4c0, 0.5, 7, 2);\n"
    "  glowB.position.set(1.98, 10.2, 2.6);\n"
    "  scene.add(glowB);")
sub("    new THREE.MeshLambertMaterial({ color: 0x2c3038 }));",
    "    new THREE.MeshStandardMaterial({ color: 0xcfccc4, roughness: 0.96, metalness: 0 }));")
sub("  ground.receiveShadow = true;\n  scene.add(ground);",
    "  ground.receiveShadow = true;\n"
    "  scene.add(ground);\n"
    "  var catcher = new THREE.Mesh(new THREE.PlaneGeometry(60, 60),\n"
    "    new THREE.ShadowMaterial({ opacity: 0.22 }));\n"
    "  catcher.position.set(1.98, 7.9, -0.195);\n"
    "  catcher.receiveShadow = true;\n"
    "  scene.add(catcher);")
sub("  ctlO.enableRotate = false;",
    "  ctlO.enableRotate = false;\n"
    "  ctlP.enableDamping = true;\n"
    "  ctlP.dampingFactor = 0.08;\n"
    "  ctlO.enableDamping = true;\n"
    "  ctlO.dampingFactor = 0.08;")
NEW_MAT = '''var TEXC = {};
function canvasTex(key, size, fn) {
  if (TEXC[key]) return TEXC[key];
  var cv = document.createElement("canvas");
  cv.width = size; cv.height = size;
  fn(cv.getContext("2d"), size);
  var tx = new THREE.CanvasTexture(cv);
  tx.wrapS = THREE.RepeatWrapping; tx.wrapT = THREE.RepeatWrapping;
  tx.encoding = THREE.sRGBEncoding;
  TEXC[key] = tx;
  return tx;
}
function woodTex() {
  return canvasTex("wood", 256, function (c, S) {
    c.fillStyle = "#cda878"; c.fillRect(0, 0, S, S);
    var y;
    for (y = 0; y < S; y += 2) {
      var v = Math.sin(y * 0.35) * 8 + Math.sin(y * 0.09) * 10;
      c.fillStyle = "rgba(120,80,40," + (0.05 + 0.05 * Math.abs(v) / 18) + ")";
      c.fillRect(0, y, S, 1);
    }
    c.fillStyle = "rgba(90,60,30,0.55)";
    for (y = 0; y <= S; y += 64) c.fillRect(0, y, S, 2);
  });
}
function fabricTex() {
  return canvasTex("fabric", 128, function (c, S) {
    c.fillStyle = "#ffffff"; c.fillRect(0, 0, S, S);
    var i, x, yy;
    for (i = 0; i < 2600; i++) {
      x = (i * 73) % S; yy = (i * 149) % S;
      c.fillStyle = (i % 2) ? "rgba(0,0,0,0.05)" : "rgba(255,255,255,0.7)";
      c.fillRect(x, yy, 1, 1);
    }
  });
}
var BLOBMAT = null;
function blobMat() {
  if (BLOBMAT) return BLOBMAT;
  var cv = document.createElement("canvas");
  cv.width = 128; cv.height = 128;
  var c = cv.getContext("2d");
  var g = c.createRadialGradient(64, 64, 8, 64, 64, 62);
  g.addColorStop(0, "rgba(20,18,14,0.42)");
  g.addColorStop(0.65, "rgba(20,18,14,0.18)");
  g.addColorStop(1, "rgba(20,18,14,0)");
  c.fillStyle = g; c.fillRect(0, 0, 128, 128);
  BLOBMAT = new THREE.MeshBasicMaterial({ map: new THREE.CanvasTexture(cv),
    transparent: true, depthWrite: false });
  return BLOBMAT;
}
function matFor(s) {
  var kind = s.kind || "", m = s.material || "concrete";
  var isNew = (kind === "new_partition" || kind === "glass" ||
               kind === "mullion" || kind === "curtain");
  if (m === "glass") {
    return { mat: new THREE.MeshPhysicalMaterial({ color: isNew ? 0xe8934a : 0xcfe0ee,
      roughness: 0.08, metalness: 0, transparent: true,
      opacity: isNew ? 0.34 : 0.24, side: THREE.DoubleSide,
      depthWrite: false, polygonOffset: true, polygonOffsetFactor: 1,
      polygonOffsetUnits: 1 }), isNew: isNew };
  }
  var p = { color: 0xcccccc, roughness: 0.9, metalness: 0.02 };
  if (m === "concrete") { p.color = 0xe6e1d5; p.roughness = 0.95; }
  if (m === "stud") { p.color = 0xeae4d5; p.roughness = 0.9; }
  if (m === "floor") { p.color = 0xffffff; p.map = woodTex(); p.roughness = 0.65; }
  if (m === "wood") { p.color = 0xd8b285; p.map = woodTex(); p.roughness = 0.6; }
  if (m === "fabric") { p.color = 0x9db9d9; p.map = fabricTex(); p.roughness = 1.0; }
  if (m === "porcelain") { p.color = 0xffffff; p.roughness = 0.32; }
  if (m === "ceiling") { p.color = 0xf2f0ea; p.roughness = 1.0; }
  if (kind === "slab" && m === "concrete") {
    p.color = 0xffffff; p.map = woodTex(); p.roughness = 0.7; }
  if (kind === "new_partition" || kind === "mullion") {
    p.color = 0xe8590c; p.roughness = 0.55;
    p.emissive = 0x7a2a00; p.emissiveIntensity = 0.35; }
  if (kind === "curtain") {
    p.color = 0xe8894a; p.roughness = 0.9;
    p.transparent = true; p.opacity = 0.5; p.side = THREE.DoubleSide;
    p.depthWrite = false;
    p.emissive = 0x5a2400; p.emissiveIntensity = 0.25; }
  return { mat: new THREE.MeshStandardMaterial(p), isNew: isNew };
}
''';
rep_between("function matFor(s) {", "function isWallKind(k) {", NEW_MAT)
sub("  S.labels = []; S.wallMeshes = []; S.ceilMeshes = []; S.furnMeshes = [];",
    "  S.labels = []; S.wallMeshes = []; S.ceilMeshes = []; S.furnMeshes = []; S.fxMeshes = [];")
sub("    mesh.receiveShadow = true;",
    "    mesh.receiveShadow = true;\n"
    "    if (isFurnKind(k)) {\n"
    "      var edge = new THREE.LineSegments(new THREE.EdgesGeometry(mesh.geometry),\n"
    "        new THREE.LineBasicMaterial({ color: 0x3a3f47, transparent: true, opacity: 0.16 }));\n"
    "      edge.position.copy(mesh.position);\n"
    "      S.group.add(edge);\n"
    "      S.fxMeshes.push(edge);\n"
    "      if ((s.z || 0) <= 50) {\n"
    "        var blob = new THREE.Mesh(\n"
    "          new THREE.PlaneGeometry(w * 1.25 + 0.14, d * 1.25 + 0.14), blobMat());\n"
    "        blob.position.set(((s.x || 0) * U) + w / 2, ((s.y || 0) * U) + d / 2,\n"
    "          ((s.z || 0) * U) + 0.012);\n"
    "        blob.renderOrder = 1;\n"
    "        S.group.add(blob);\n"
    "        S.fxMeshes.push(blob);\n"
    "      }\n"
    "    }")
sub("  for (i = 0; i < S.furnMeshes.length; i++) S.furnMeshes[i].visible = S.showFurn;",
    "  for (i = 0; i < S.furnMeshes.length; i++) S.furnMeshes[i].visible = S.showFurn;\n"
    "  for (i = 0; i < S.fxMeshes.length; i++) S.fxMeshes[i].visible = S.showFurn;")
sub("    var dist = c.r * 1.30;\n"
    "    S.persp.position.set(c.x - dist * 0.30, c.y - dist * 0.62, dist * 0.30);",
    "    var dist = c.r * 1.22;\n"
    "    S.persp.position.set(c.x - dist * 0.34, c.y - dist * 0.58, dist * 0.40);")
TPL.write_text(t, encoding="utf-8")
print("commercial pass applied, bytes:", len(t))

