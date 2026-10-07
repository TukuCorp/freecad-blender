await page.setViewportSize({ width: 375, height: 812 });
await page.goto("http://localhost:64809/docs/contractor-as-drawn-light.html", { waitUntil: "domcontentloaded" });
await page.waitForTimeout(5000);
const info = await page.evaluate(() => {
  const o = document.getElementById('overlay');
  const b = document.getElementById('build-badge');
  const v = window.__viewer;
  return {
    overlayHidden: o ? o.classList.contains('hidden') : null,
    badge: b ? b.textContent.trim() : null,
    viewerReady: !!v,
    canvasSize: v ? { w: v.renderer.domElement.width, h: v.renderer.domElement.height } : null
  };
});
console.log(JSON.stringify(info));
await page.screenshot({ path: "C:/Users/tukum/Downloads/freecad-blender/tmp/critic-375x812.png" });
return info;
