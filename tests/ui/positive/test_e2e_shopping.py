import allure
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.demoblaze
@allure.title("E2E: Full Checkout Flow (Login to Purchase)")
def test_full_checkout_flow(page, login_page: LoginPage, product_page, cart_page, checkout_page):
    """
    Business Flow:
    1. Login with valid credentials using LoginPage
    2. Select product and handle the 'Product added' dialog
    3. Verify product presence in the CartPage
    4. Complete checkout via CheckoutPage
    5. Verify success and perform logout
    """

    # --- STEP 1: LOGIN ---
    page.goto("https://www.demoblaze.com/")
    with allure.step("Step 1: Login to the system"):
        # We now use the specialized LoginPage class
        login_page.open_modal()
        login_page.submit_login("test", "test")

        # Verification that login was successful (Welcome message)
        # Using the locator from page directly to keep ProductPage clean
        expect(page.locator("#nameofuser")).to_contain_text("Welcome test")

    # --- STEP 2: ADD PRODUCT ---
    with allure.step("Step 2: Add product to cart"):
        # Navigation to product is still handled by a generic page action or direct URL
        page.goto("https://www.demoblaze.com/prod.html?idp_=1")

        # Using the new 'clean' method that only clicks
        with page.expect_event("dialog") as dialog_info:
            product_page.click_add_to_cart()

        # Explicitly handling the success dialog in the test
        assert "Product added" in dialog_info.value.message
        dialog_info.value.accept()

    # --- STEP 3: PROCEED TO CHECKOUT ---
    with allure.step("Step 3: Open cart and verify product"):
        cart_page.open_cart()
        assert cart_page.is_product_in_cart("Samsung galaxy s6")
        cart_page.click_place_order()

    # --- STEP 4: SUBMIT PURCHASE FORM ---
    with allure.step("Step 4: Submit purchase form"):
        checkout_page.submit_order(
            name="QA Tester",
            country="Spain",
            city="Valencia",
            card="1234-5678-9012"
        )

    # --- STEP 5: VERIFY & LOGOUT ---
    with allure.step("Step 5: Verify purchase success and logout"):
        message = checkout_page.get_confirmation_text()
        assert "Thank you for your purchase!" in message

        # Final cleanup: Logout
        page.click("#logout2")
        expect(page.locator("#login2")).to_be_visible()