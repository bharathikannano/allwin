const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: 1280, height: 720 } });
  const page = await context.newPage();

  console.log("Navigating to http://localhost:5173/");
  await page.goto('http://localhost:5173/');
  await page.waitForTimeout(2000); // Wait for data to load

  await page.screenshot({ path: 'dashboard.png' });
  console.log("Screenshot saved as dashboard.png");

  console.log("Navigating to http://localhost:5173/logs");
  await page.goto('http://localhost:5173/logs');
  await page.waitForTimeout(2000); // Wait for data to load
  await page.screenshot({ path: 'logs.png' });
  console.log("Screenshot saved as logs.png");

  await browser.close();
})();
