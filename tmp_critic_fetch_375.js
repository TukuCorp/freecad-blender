await page.setViewportSize({ width: 375, height: 812 });
await page.goto("http://localhost:8765/tmp_viewer.html", { waitUntil: "domcontentloaded" });
await page.waitForTimeout(8000);
await page.waitForFunction(() => {
  const el = document.getElementById('overlay');
  return el && el.classList.contains('hidden');
}, null, { timeout: 20000 }).catch(()=>{});
await page.waitForTimeout(2000);
const out = "C:/Users/tukum/Downloads/freecad-blender/tmp/critic-375x812.png";
await page.screenshot({ path: out, fullPage: false });
return { viewport: page.viewportSize(), url: page.url(), overlayHidden: await page.evaluate(()=> document.getElementById('overlay')?.classList.contains('hidden')), out };
