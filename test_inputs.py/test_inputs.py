from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # --- PART 1: Checkbox Test ---
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Pehla checkbox check (tick) karo
    page.locator("input[type='checkbox']").first.check()
    print("Pehla checkbox checked:", page.locator("input[type='checkbox']").first.is_checked())

    # Dusra checkbox uncheck (untick) karo
    page.locator("input[type='checkbox']").last.uncheck()
    print("Dusra checkbox checked:", page.locator("input[type='checkbox']").last.is_checked())

    # --- PART 2: Dropdown Test ---
    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Dropdown me se 'Option 2' select karo value ke through
    page.locator("#dropdown").select_option("2")
    print("Dropdown Option 2 successfully select ho gaya!")

    browser.close()