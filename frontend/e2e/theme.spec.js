import { test, expect } from '@playwright/test';

test('theme toggle functionality', async ({ page }) => {
  // 1. Visit Home Page
  await page.goto('http://localhost:5173/');

  // Wait for hydration
  await page.waitForLoadState('networkidle');

  // Check default theme (Dark)
  // We check the computed background color of the body
  const body = page.locator('body');
  await expect(body).toHaveCSS('background-color', 'rgb(15, 15, 15)'); // #0f0f0f

  // 2. Toggle to Light Theme
  const toggleBtn = page.getByLabel('Toggle Theme');
  await toggleBtn.click();

  // Check if theme changed to Light
  await expect(body).toHaveCSS('background-color', 'rgb(255, 255, 255)'); // #ffffff
  
  // Verify HTML class
  const html = page.locator('html');
  await expect(html).toHaveClass(/light/);

  // 3. Persistence Check
  await page.reload();
  await page.waitForLoadState('networkidle');

  // Should still be Light
  await expect(body).toHaveCSS('background-color', 'rgb(255, 255, 255)');
  await expect(html).toHaveClass(/light/);

  // 4. Toggle back to Dark
  await toggleBtn.click();

  // Check if theme changed back to Dark
  await expect(body).toHaveCSS('background-color', 'rgb(15, 15, 15)');
  await expect(html).toHaveClass(/dark/);
});
