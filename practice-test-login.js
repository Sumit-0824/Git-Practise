const { chromium } = require('playwright');

const loginUrl = 'https://practicetestautomation.com/practice-test-login/';

async function main() {
  const browser = await chromium.launch({ headless: false });

  try {
    const page = await browser.newPage();
    await page.goto(loginUrl);
    await page.getByLabel('Username').fill('student');
    await page.getByLabel('Password').fill('Password123');
    await page.getByRole('button', { name: 'Submit' }).click();

    await page.waitForURL('**/logged-in-successfully/');
    await page.getByText(/Congratulations|successfully logged in/i).waitFor({
      state: 'visible',
    });
    await page.getByText('Log out', { exact: true }).waitFor({
      state: 'visible',
    });

    console.log('Login successful');
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
