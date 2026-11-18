from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # 1. Login page par jao
    page.goto("https://the-internet.herokuapp.com/login")

    # 2. Username aur password bharo
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")

    # 3. Login par click karo
    page.locator("button[type='submit']").click()

    # 4. Ab naya step: Logout button dhoondh kar uspe click karo
    # Yahan hum role aur name use kar rahe hain
    page.get_by_role("link", name="Logout").click()

    # 5. Check karo ki wapas Login page ka text aa gaya ya nahi
    logout_message = page.locator("#flash").inner_text()
    print("Logout ke baad result:", logout_message)

    browser.close()