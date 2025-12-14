import { test, expect } from '@playwright/test';

test('add a movie review', async ({ page }) => {
  // Use the service name from docker-compose and the internal port
  await page.goto('http://flask-service:5000/');
  await page.getByTestId('reviewTxtField').fill('Great movie!');
  await page.getByTestId('submitReviewBtn').click();
});
