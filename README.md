# Practice Login Test Framework

This pytest framework uses JSON test data, a Page Object Model, shared browser
fixtures, and pytest-html reporting for the Practice Test Automation login page.

## Setup

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run

Run headless:

```powershell
python -m pytest
```

Run with a visible Chromium window:

```powershell
python -m pytest --headed
```

The HTML report is written to `reports/report.html`. When a test fails, the
framework saves a full-page PNG under `reports/screenshots/` and embeds it in
the corresponding HTML report entry.
