from playwright.sync_api import sync_playwright

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        # Open the login page
        page.goto("https://the-internet.herokuapp.com/login")

        # Enter invalid credentials
        page.locator("#username").fill("wrong_user")
        page.locator("#password").fill("WrongPassword123!")

        # Click the login button
        page.locator("button[type='submit']").click()

        # Verify the error message
        error_message = page.locator("#flash").inner_text()
        print("Error Message:", error_message)

        assert "Your username is invalid!" in error_message
        print("Test Passed: Invalid login properly blocked!")

        browser.close()

test_invalid_login()