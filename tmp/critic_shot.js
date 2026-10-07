const PORT = require('fs').readFileSync('tmp/server_port.txt','utf8').trim();
const path = require('path');
async function shoot(viewport, urlPath, outPath) {
  await page.setViewportSize(viewport);
  await page.goto(`http://localhost:${PORT}/${urlPath}`, { waitUntil: 'domcontentloaded' });
  // Wait for model to load and overlay hidden
  await page.waitForTimeout(3000);
  // Check overlay hidden, badge
  const overlayHidden = await page.evaluate(() => {
    const o = document.getElementById('overlay');
    return o ? o.classList.contains('hidden') : null;
  });
  const badge = await page.evaluate(() => {
    const b = document.getElementById('build-badge');
    return b ? b.textContent.trim() : null;
  });
  const header = await page.evaluate(() => {
    const b64 = window._b64 || '';
    // Instead check via decoding first bytes if available via window.__viewer
    return document.documentElement.outerHTML.slice(0,500);
  });
  console.log(`overlayHidden=${overlayHidden} badge=${badge} viewport=${viewport.width}x${viewport.height}`);
  // Hide HUD badge? keep visible but overlay should be hidden per spec
  // Take screenshot
  await page.screenshot({ path: outPath, fullPage: false });
  console.log(`shot ${outPath}`);
  return { overlayHidden, badge };
}
