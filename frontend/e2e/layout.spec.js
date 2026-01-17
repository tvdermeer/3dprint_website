import { test, expect } from '@playwright/test';

test('header and footer have correct layout classes', async ({ page }) => {
  await page.goto('http://localhost:5173/');

  // Check Header Container
  const headerContainer = page.locator('header .container');
  await expect(headerContainer).toHaveClass(/mx-auto/);
  await expect(headerContainer).toHaveClass(/px-4/);
  await expect(headerContainer).toHaveClass(/md:px-6/);

  // Check Footer Container
  const footerContainer = page.locator('footer .container');
  await expect(footerContainer).toHaveClass(/mx-auto/);
  await expect(footerContainer).toHaveClass(/px-4/);
  await expect(footerContainer).toHaveClass(/md:px-6/);
});

test('product page has correct layout classes', async ({ page }) => {
  await page.goto('http://localhost:5173/product');

  // Check Main Content Container
  // The structure is: div.min-h-dvh > div.container
  // We can target it by finding the container that isn't the header or footer
  // Or explicitly looking for the one inside the main wrapper
  
  const mainContainer = page.locator('.min-h-dvh > .container');
  await expect(mainContainer).toHaveClass(/mx-auto/);
  await expect(mainContainer).toHaveClass(/px-4/);
  await expect(mainContainer).toHaveClass(/md:px-6/);
});
