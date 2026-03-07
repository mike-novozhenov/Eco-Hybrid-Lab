import pytest
import allure
from playwright.sync_api import Page, TimeoutError


@pytest.mark.ui
@allure.title("Test Case 1: Pure UI - Add Product to Cart")
def test_add_samsung_to_cart(product_page, cart_page, page: Page):
    target_product = "Samsung galaxy s6"

    with allure.step("Prepare browser state"):
        page.goto("https://www.demoblaze.com/index.html")

    with allure.step("Open product page for target item"):
        product_page.navigate("prod.html?idp_=1")

    with allure.step("Add product to cart and handle confirmation alert"):
        with page.expect_event("dialog") as dialog_info:
            product_page.click_add_to_cart()

        assert "Product added" in dialog_info.value.message
        dialog_info.value.accept()

    with allure.step("Verify product in cart"):
        cart_page.open_cart()

        try:
            page.wait_for_selector("#tbodyid tr", timeout=2000)
        except TimeoutError:
            allure.attach(page.screenshot(), name="Empty Cart Error", attachment_type=allure.attachment_type.PNG)

        allure.attach(
            page.screenshot(full_page=True), name="Cart Final State", attachment_type=allure.attachment_type.PNG
        )

        is_present = cart_page.is_product_in_cart(target_product)
        assert is_present, (
            f"Verification Failed! Expected to find '{target_product}' in the cart, "
            f"but it was missing. Check 'Cart Final State' attachment for details"
        )
