from playwright.sync_api import Browser, BrowserContext, Playwright


def launch_browser(playwright: Playwright, *, headless: bool = True) -> Browser:
    return playwright.chromium.launch(headless=headless)


def create_browser_context(browser: Browser) -> BrowserContext:
    return browser.new_context(viewport={"width": 1280, "height": 720})
