from playwright.sync_api import Page
from typing import Literal

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.demoblaze.com/"

    def navigate(self, path: str = ""):
        """Navigates to the specified path relative to base URL"""
        return self.page.goto(f"{self.base_url}{path}")

    def click(self, selector: str):
        """Waits for element and performs a click"""
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def get_text(self, selector: str) -> str:
        """Returns the inner text of an element"""
        self.page.wait_for_selector(selector)
        return self.page.inner_text(selector)

    def wait_for_load_state(self, state: Literal["domcontentloaded", "load", "networkidle"] = "networkidle"):
        """Waits for a specific network state"""
        self.page.wait_for_load_state(state)