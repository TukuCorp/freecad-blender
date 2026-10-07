await page.setViewportSize({ width: 1280, height: 720 });
const fileUrl = "file:///C:/Users/tukum/Downloads/freecad-blender/docs/contractor-as-drawn.html";
await page.goto(fileUrl, { waitUntil: "domcontentloaded" });
await page.waitForTimeout(7000);
// check overlay hidden
await page.waitForFunction(() => {
  const el = document.getElementById('overlay');
  return el && el.classList.contains('hidden');
}, null, { timeout: 15000 }).catch(()=>{});
await page.waitForTimeout(2000);
// take screenshot
const out = "C:/Users/tukum/Downloads/freecad-blender/tmp/critic-1280x720.png";
await page.screenshot({ path: out, fullPage: false });
return { title: await page.title(), url: page.url(), viewport: page.viewportSize(), out, overlayHidden: await page.evaluate(()=> document.getElementById('overlay')?.classList.contains('hidden') ), errors: await page.evaluate(()=> document.body.innerHTML.slice(0,500)) };
