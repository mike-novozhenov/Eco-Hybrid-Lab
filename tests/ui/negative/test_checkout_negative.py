import allure
import pytest


@pytest.mark.ui
@pytest.mark.negative
@allure.title("Negative: Validate empty checkout form (No-Wait Flow)")
def test_purchase_with_empty_fields_ui(page, cart_page, checkout_page):
    # --- STEP 0: NETWORK OPTIMIZATION ---
    # Abort heavy assets to speed up page loading
    page.route("**/*.{png,jpg,jpeg,svg,css}", lambda route: route.abort())

    # --- STEP 1: ADD PRODUCT ---
    with allure.step("Step 1: Quick add and go"):
        # We go home and then immediately to a product (first one)
        page.goto("https://www.demoblaze.com/index.html", wait_until="commit")
        page.locator(".card-title a").first.click()

        # Non-blocking dialog handler
        page.once("dialog", lambda d: d.accept())
        page.locator("a.btn-success").click()

    # --- STEP 2: BYPASS CART LOADING ---
    with allure.step("Step 2: Instant Place Order"):
        # Go to cart page
        page.goto("https://www.demoblaze.com/cart.html", wait_until="commit")

        # Click Place Order immediately without waiting for product rows
        # force=True skips actionability checks (like 'is it covered by a loader?')
        page.locator("button.btn-success").click(force=True)

    # --- STEP 3: TRIGGER ALERT ---
    with allure.step("Step 3: Handle validation alert"):
        # Catch the "Please fill out Name and Creditcard."
        page.once("dialog", lambda d: d.accept())
        checkout_page.click_purchase()

    # --- STEP 4: VERIFY ---
    with allure.step("Step 4: Verify modal state"):
        assert checkout_page.is_modal_visible()