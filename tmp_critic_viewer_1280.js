await page.setViewportSize({ width: 1280, height: 720 });
const fileUrl = "file:///C:/Users/tukum/Downloads/freecad-blender/docs/contractor-as-drawn.html";
await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
await page.waitForTimeout(6000);
// wait for three.js to render - check for canvas content
await page.waitForFunction(() => {
  const canvas = document.getElementById('viewer');
  return canvas && canvas.width > 0;
}, null, { timeout: 10000 }).catch(()=>{});
await page.waitForTimeout(3000);
// try reset view button
const overlay = await page.locator('#overlay.hidden').count().catch(()=>0);
await page.waitForTimeout(1000);
const fs = require('fs');
const path = require('path');
const out = path.resolve("C:/Users/tukum/Downloads/freecad-blender/tmp/critic-1280x720.png");
await page.screenshot({ path: out, fullPage: false });
return { title: await page.title(), url: page.url(), viewport: page.viewportSize(), out, overlayHidden: await page.evaluate(()=> document.getElementById('overlay')?.classList.contains('hidden')) };
