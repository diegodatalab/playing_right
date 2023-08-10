from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(
        headless=False,
        slow_mo=5000
    )

    page = browser.new_page()
    page.goto('https://bootswatch.com/default')

    button = page.get_by_role('button', name='Primary').first
    button.click()

    browser.close()