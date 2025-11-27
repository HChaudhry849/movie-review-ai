import { test, expect } from '@playwright/test';

test('add a movie review', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/');
  await page.getByTestId('reviewTxtField').fill('Great movie!');
  await page.getByTestId('submitReviewBtn').click();
});