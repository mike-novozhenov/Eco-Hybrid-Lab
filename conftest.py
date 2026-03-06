import os
import pytest
import allure
from dotenv import load_dotenv

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.api_client import ApiClient
from utils.db_client import DbClient
from pages.home_page import HomePage

# Load environment variables
load_dotenv()


@pytest.fixture(scope="function")
def api_client():
    """Provides a clean API client instance for each test"""
    return ApiClient()


@pytest.fixture
def product_page(page):
    """Initializes Product Page and navigates to the base URL"""
    url = os.getenv("BASE_URL")
    if url:
        page.goto(url)
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    """Provides access to Cart Page actions"""
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    """Provides access to Checkout Page actions"""
    return CheckoutPage(page)


@pytest.fixture(autouse=True)
def cleanup_after_test(request):
    """
    Handles post-test cleanup (cookies, storage).
    Failure screenshots are now handled by the global hook for better stability.
    Uses safe access to avoid errors if the page is already closed.
    """
    yield

    # Safe access to the page fixture via funcargs
    page = request.node.funcargs.get("page")

    if page:
        try:
            if not page.is_closed():
                with allure.step("Cleanup: Resetting browser state"):
                    page.context.clear_cookies()
                    page.evaluate("window.localStorage.clear()")
                    page.evaluate("window.sessionStorage.clear()")
        except (RuntimeError, ValueError, AttributeError, KeyError):
            # Silent fallback if the page context is already destroyed
            pass


@pytest.fixture
def db_client():
    """
    Database fixture with automated Setup and Teardown.
    """
    client = DbClient("test_database.db")
    client.execute_query(
        "CREATE TABLE IF NOT EXISTS test_logs (id INTEGER PRIMARY KEY, action TEXT, status TEXT)"
    )
    yield client
    with allure.step("DB Cleanup: Removing test records"):
        client.execute_query("DELETE FROM test_logs")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Captures a screenshot on failure immediately after the test call phase.
    Works for any UI test that uses the 'page' fixture.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Retrieve the page instance from test arguments
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Failure_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

    if report.when == "call":
        setattr(item, "rep_call", report)

@pytest.fixture
def home_page(page):
    return HomePage(page)

from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)