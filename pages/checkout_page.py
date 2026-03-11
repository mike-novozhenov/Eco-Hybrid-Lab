import allure
from playwright.sync_api import TimeoutError
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.name_field = page.locator("#name")
        self.country_field = page.locator("#country")
        self.city_field = page.locator("#city")
        self.card_field = page.locator("#card")
        self.month_field = page.locator("#month")
        self.year_field = page.locator("#year")
        self.purchase_button = page.locator("button[onclick='purchaseOrder()']")
        self.success_message = page.locator(".sweet-alert h2")
        self.confirm_button = page.locator("button.confirm")
        self.order_modal = page.locator("#orderModal")
        self.close_modal_button = page.locator("#orderModal .btn-secondary").get_by_text("Close")

    @allure.step("Checkout: Submit order for {name}")
    def submit_order(self, name, country, city, card):
        """Fills the form and clicks purchase in one business action"""
        self.name_field.wait_for(state="visible")
        self.name_field.fill(name)
        self.country_field.fill(country)
        self.city_field.fill(city)
        self.card_field.fill(card)
        self.month_field.fill("12")
        self.year_field.fill("2026")
        self.purchase_button.click()
        self.success_message.wait_for(state="visible")

    @allure.step("Checkout: Verify and finalize")
    def get_confirmation_text(self):
        """Captures confirmation and cleans up modals"""
        text = self.success_message.inner_text()
        self.confirm_button.click()
        try:
            self.order_modal.wait_for(state="hidden", timeout=2000)
        except TimeoutError:
            if self.order_modal.is_visible():
                self.close_modal_button.click()
                self.order_modal.wait_for(state="hidden")
        return text

    @allure.step("Checkout: Click 'Purchase' button")
    def click_purchase(self):
        """Click the purchase button without any actionability checks"""
        self.purchase_button.dispatch_event("click")

    @allure.step("Checkout: Check if modal is still visible")
    def is_modal_visible(self) -> bool:
        """Verify that the order modal did not close"""
        try:
            self.order_modal.wait_for(state="visible", timeout=1000)
            return True
        except (TimeoutError, Exception):
            return False
