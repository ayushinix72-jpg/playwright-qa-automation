from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        # Browser kholo (headless=False taaki screen par dikhe)
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        # 1. Login page par jao
        page.goto("https://the-internet.herokuapp.com/login")
        
        # 2. Username aur Password enter karo
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        
        # 3. Login button par click karo
        page.locator("button[type='submit']").click()
        
        # 4. Check karo ki login successful hua ya nahi
        success_message = page.locator("#flash").inner_text()
        print("Login Result:", success_message)
        
        assert "You logged into a secure area!" in success_message
        print("Test Passed: Successfully logged in!")
        
        browser.close()