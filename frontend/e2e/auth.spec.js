import { test, expect } from '@playwright/test';

test('auth flow - signup, login, logout', async ({ page }) => {
  // Generate random email for test
  const email = `test-${Math.random().toString(36).substring(7)}@example.com`;
  const password = 'TestPassword123!';

  // 1. Visit Login Page
  await page.goto('http://localhost:5173/login');
  await expect(page).toHaveURL('http://localhost:5173/login');

  // 2. Sign Up
  // Toggle to signup mode
  await page.getByRole('button', { name: 'Sign up' }).click();
  await expect(page.getByRole('heading', { name: 'Create Account' })).toBeVisible();

  // Fill form
  await page.getByPlaceholder('John Doe').fill('Test User');
  await page.getByPlaceholder('your@email.com').fill(email);
  await page.getByPlaceholder('••••••••').fill(password);
  
  // Submit
  page.on('dialog', dialog => dialog.accept()); // Handle alert
  await page.getByRole('button', { name: 'Sign Up' }).click();
  
  // Wait for success/switch to login
  await expect(page.getByRole('heading', { name: 'Welcome Back' })).toBeVisible();

  // 3. Login
  await page.getByPlaceholder('your@email.com').fill(email);
  await page.getByPlaceholder('••••••••').fill(password);
  await page.getByRole('button', { name: 'Log In' }).click();

  // Verify redirect to home
  await expect(page).toHaveURL('http://localhost:5173/');
  
  // Verify user is logged in (check header)
  await expect(page.locator('header')).toContainText(email);

  // 4. Logout
  await page.locator('header button').click(); // Logout button
  await expect(page.locator('header')).not.toContainText(email);
});
