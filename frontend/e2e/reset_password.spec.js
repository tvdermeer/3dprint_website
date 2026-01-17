import { test, expect } from '@playwright/test';

test('password recovery flow', async ({ page }) => {
  // 1. Visit Login Page
  await page.goto('http://localhost:5173/login');

  // 2. Go to Forgot Password
  await page.click('text=Forgot your password?');
  await expect(page.getByRole('heading', { name: 'Reset Password' })).toBeVisible();

  // 3. Request Reset
  await page.getByPlaceholder('your@email.com').fill('test@example.com');
  await page.getByRole('button', { name: 'Send Reset Link' }).click();
  
  await expect(page.getByText('If an account exists, a recovery email has been sent.')).toBeVisible();
});

test('password reset page validation', async ({ page }) => {
  // Visit with a fake token
  await page.goto('http://localhost:5173/reset-password?token=fake-token');

  // Check validation
  await page.getByPlaceholder('New Password').fill('weak');
  await expect(page.getByText('Password must be at least 8 characters long')).toBeVisible();

  // Fill valid password but mismatch confirm
  await page.getByPlaceholder('New Password').fill('StrongPass1!');
  await page.getByPlaceholder('Confirm Password').fill('DifferentPass1!');
  await page.getByRole('button', { name: 'Reset Password' }).click();
  
  await expect(page.getByText('Passwords do not match')).toBeVisible();
});
