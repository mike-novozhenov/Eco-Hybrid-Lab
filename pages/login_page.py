import allure

class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.login_menu_link = page.locator("#login2")
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.login_button = page.get_by_role("button", name="Log in")
        self.close_button = page.locator("#logInModal >> .btn-secondary")

    @allure.step("Open Login modal window")
    def open_modal(self):
        """Clicks the login link in the header and waits for the modal to appear"""
        self.login_menu_link.click()
        # Ensure the modal is visible before interaction
        self.username_input.wait_for(state="visible", timeout=5000)

    @allure.step("Submit login credentials: {username}")
    def submit_login(self, username, password):
        """Fills in credentials and clicks the login button"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()