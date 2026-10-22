from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.pokemon.com/us/pokedex")
    page.locator(".results").filter(has_text="0001").click()
    print(page.title())
    browser.close()
