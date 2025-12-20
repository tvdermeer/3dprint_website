import { test, expect } from '@playwright/test';

test('full checkout flow', async ({ page }) => {
  // 1. Visit Home
  await page.goto('http://localhost:5173/');
  await expect(page).toHaveTitle(/Vite App/); // Or whatever title is configured

  // 2. Navigate to Product (Header navigation)
  await page.locator('nav').getByRole('link', { name: 'Product' }).click();
  await expect(page).toHaveURL('http://localhost:5173/product');
  
  // Wait for product to load
  await expect(page.getByRole('heading', { level: 1 })).not.toContainText('Loading');

  // 3. Add to Cart
  await page.getByRole('button', { name: /Add to Cart/ }).click();
  
  // 4. Go to Checkout (via cart count/link or direct link)
  await page.getByRole('link', { name: /Checkout/ }).click();
  await expect(page).toHaveURL('http://localhost:5173/checkout');

  // 5. Verify Cart Contents
  await expect(page.getByRole('heading', { name: 'Shopping Cart' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Proceed to Checkout' })).toBeVisible();

  // 6. Proceed to Payment
  await page.getByRole('button', { name: 'Proceed to Checkout' }).click();
  await expect(page.getByRole('heading', { name: 'Payment Information' })).toBeVisible();

  // 7. Fill Form
  await page.locator('input[name="email"]').fill('test@example.com');
  await page.locator('input[name="name"]').fill('Test User');
  await page.locator('input[name="address"]').fill('123 Test St');
  await page.locator('input[name="city"]').fill('Test City');
  await page.locator('input[name="zipCode"]').fill('12345');
  await page.locator('input[name="cardNumber"]').fill('4242424242424242');
  await page.locator('input[name="expiryDate"]').fill('12/26');
  await page.locator('input[name="cvv"]').fill('123');

  // 8. Place Order
  await page.getByRole('button', { name: 'Place Order' }).click();

  // 9. Verify Success
  await expect(page.getByRole('heading', { name: 'Order Confirmed!' })).toBeVisible({ timeout: 10000 });
  
  // 10. Return Home
  await page.getByRole('link', { name: 'Back to Home' }).click();
  await expect(page).toHaveURL('http://localhost:5173/');
});
