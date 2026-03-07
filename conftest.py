import os
import pytest
import allure
from dotenv import load_dotenv

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.api_client import ApiClient
from utils.db_client import DbClient

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


@pytest.fixture
def home_page(page):
    """Provides access to Home Page actions"""
    return HomePage(page)


@pytest.fixture
def login_page(page):
    """Provides access to Login Page actions"""
    return LoginPage(page)


@pytest.fixture(autouse=True)
def cleanup_after_test(request):
    """
    Handles post-test cleanup (cookies, storage).
    Uses specific exceptions to avoid 'too broad exception' warnings.
    """
    yield

    page = request.node.funcargs.get("page")

    if page and not page.is_closed():
        try:
            with allure.step("Cleanup: Resetting browser state"):
                page.context.clear_cookies()
                page.evaluate("window.localStorage.clear()")
                page.evaluate("window.sessionStorage.clear()")
        except (RuntimeError, AttributeError):
            # Catch only technical errors related to closed page access
            pass


@pytest.fixture
def db_client():
    """
    Database fixture with automated Setup and Teardown.
    """
    client = DbClient("test_database.db")
    # language=SQL
    client.execute_query("CREATE TABLE IF NOT EXISTS test_logs (id INTEGER PRIMARY KEY, action TEXT, status TEXT)")
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
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True), name="Failure_Screenshot", attachment_type=allure.attachment_type.PNG
            )

    if report.when == "call":
        setattr(item, "rep_call", report)
