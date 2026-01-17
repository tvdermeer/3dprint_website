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
  
  // Test weak password
  await page.getByPlaceholder('••••••••').fill('weak');
  // Check for validation error (red border or error message)
  await expect(page.getByText('Password must be at least 8 characters long')).toBeVisible();
  await expect(page.getByPlaceholder('••••••••')).toHaveClass(/border-red-500/);

  // Fix password
  await page.getByPlaceholder('••••••••').fill(password);
  await expect(page.getByText('Password must be at least 8 characters long')).toBeHidden();

  // Submit
  page.on('dialog', dialog => dialog.accept()); // Handle alert
  await page.getByRole('button', { name: 'Sign Up' }).click();
  
  // Wait for success/switch to login
  await expect(page.getByRole('heading', { name: 'Welcome Back' })).toBeVisible();

  // 3. Login
  await page.getByPlaceholder('your@email.com').fill(email);
  await page.getByPlaceholder('••••••••').fill(password);
  await page.getByRole('button', { name: 'Log In' }).click();

  // Verify redirect to dashboard
  await expect(page).toHaveURL('http://localhost:5173/dashboard');
  
  // Verify user is logged in (check header for full name)
  await expect(page.locator('header')).toContainText('Test User');

  // 4. Logout
  await page.getByLabel('Logout').click(); // Logout button
  await expect(page.locator('header')).not.toContainText('Test User');
});
