from pages.base_page import BasePage


class CartPage(BasePage):
    # Selectors
    CART_ITEMS_TABLE = "#tbodyid"

    def open_cart(self):
        """Navigates directly to the cart page"""
        self.navigate("cart.html")

    def is_product_in_cart(self, product_name: str) -> bool:
        """Checks if the specific product is visible in the cart table"""
        selector = f"tr:has-text('{product_name}')"
        # We wait for the table to load content
        self.page.wait_for_selector(self.CART_ITEMS_TABLE)
        return self.page.is_visible(selector)