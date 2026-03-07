from playwright.sync_api import TimeoutError
from pages.base_page import BasePage


class CartPage(BasePage):
    # Selectors
    CART_ITEMS_TABLE = "#tbodyid"
    PLACE_ORDER_BUTTON = "button[data-target='#orderModal']"
    ORDER_MODAL = "#orderModal"

    def open_cart(self):
        """Navigates directly to the cart page"""
        self.navigate("cart.html")
        # Wait for the network to settle to handle the 1-2s delay
        self.page.wait_for_load_state("networkidle")

    def is_product_in_cart(self, product_name: str) -> bool:
        """Checks if the specific product is visible in the cart table"""
        selector = f"tr:has-text('{product_name}')"
        try:
            # Short timeout to handle the 'blinking' table effect
            self.page.wait_for_selector(self.CART_ITEMS_TABLE, timeout=5000)
            return self.page.is_visible(selector)
        except TimeoutError:
            return False

    def click_place_order(self):
        """Clicks the 'Place Order' button and waits for the modal to appear"""
        # We wait specifically for the button to be visible and attached
        # This solves the issue when the page is still 'blinking'
        self.page.wait_for_selector(self.PLACE_ORDER_BUTTON, state="visible", timeout=10000)
        self.page.click(self.PLACE_ORDER_BUTTON)

        # Wait until the modal actually pops up
        self.page.wait_for_selector(self.ORDER_MODAL, state="visible")
