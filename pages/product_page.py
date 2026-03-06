import allure

from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = "text=Add to cart"

    @allure.step("Product: Click 'Add to cart'")
    def click_add_to_cart(self):
        """Clicks the button without handling the dialog internally"""
        self.page.locator(self.ADD_TO_CART_BUTTON).click()