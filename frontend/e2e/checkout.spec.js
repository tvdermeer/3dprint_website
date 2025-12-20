import { test, expect } from '@playwright/test';

test('full checkout flow', async ({ page }) => {
  // Mock Stripe.js and other APIs
  await page.evaluate(() => {
    window.Stripe = function() {
      return {
        elements: () => ({
          create: () => ({
            mount: () => {},
            on: () => {},
          }),
        }),
        confirmCardPayment: () => Promise.resolve({
          paymentIntent: { status: 'succeeded' },
        }),
      };
    };
  });

  await page.route('**/api/v1/payments/create-intent', route => route.fulfill({
    status: 200,
    json: { clientSecret: 'pi_mock_secret_123' },
  }));

  await page.route('**/api/v1/orders', route => route.fulfill({
    status: 200,
    json: { id: 'ord_123' },
  }));

  // Start E2E Test
  await page.goto('http://localhost:5173/product');

  // Add to cart
  await page.getByRole('button', { name: /Add to Cart/ }).click();

  // Go to checkout
  await page.getByRole('link', { name: /Checkout/ }).click();
  
  // Proceed to payment
  await page.getByRole('button', { name: 'Proceed to Checkout' }).click();

  // Fill form
  await page.locator('input[name="email"]').fill('test@example.com');
  await page.locator('input[name="name"]').fill('Test User');
  await page.locator('input[name="address"]').fill('123 Test St');
  await page.locator('input[name="city"]').fill('Test City');
  await page.locator('input[name="zipCode"]').fill('12345');

  // Place order
  await page.getByRole('button', { name: 'Place Order' }).click();

  // Verify success
  await expect(page.getByRole('heading', { name: 'Order Confirmed!' })).toBeVisible();
});
