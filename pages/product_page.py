from playwright.sync_api import Dialog  # Добавляем импорт типа
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Selectors
    ADD_TO_CART_BTN = "text=Add to cart"
    PRODUCT_NAME_HEADER = "h2.name"

    def add_to_cart(self):
        """Clicks 'Add to cart' and handles the native browser dialog"""

        # Теперь мы явно указываем, что dialog — это объект Dialog
        # Это уберет ошибку "Unresolved attribute reference 'accept'"
        def handle_dialog(dialog: Dialog):
            dialog.accept()

        self.page.on("dialog", handle_dialog)
        self.click(self.ADD_TO_CART_BTN)

    def get_product_name(self) -> str:
        """Returns the product name from the header"""
        return self.get_text(self.PRODUCT_NAME_HEADER)