from playwright.sync_api import sync_playwright

def test_checkboxes_and_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # 1. Test checkboxes
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = page.locator("input[type='checkbox']")

        # Ensure both checkboxes are checked
        first_checkbox = checkboxes.nth(0)
        second_checkbox = checkboxes.nth(1)

        if not first_checkbox.is_checked():
            first_checkbox.check()
        if not second_checkbox.is_checked():
            second_checkbox.check()

        assert first_checkbox.is_checked()
        assert second_checkbox.is_checked()

        # 2. Test dropdown selection
        page.goto("https://the-internet.herokuapp.com/dropdown")
        dropdown = page.locator("#dropdown")
        dropdown.select_option("2")

        assert dropdown.input_value() == "2"
        print("Test Passed: Checkboxes and dropdown verified!")

        browser.close()

test_checkboxes_and_dropdown()