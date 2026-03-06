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
    return ApiClient()


@pytest.fixture
def product_page(page):
    url = os.getenv("BASE_URL")
    if url:
        page.goto(url)
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture(autouse=True)
def manage_test_lifecycle(page, request):
    # Включаем трассировку
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield

    if not page.is_closed():
        try:
            # Если тест упал — сохраняем Trace
            if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
                trace_path = os.path.join("allure-results", f"trace_{request.node.name}.zip")
                page.context.tracing.stop(path=trace_path)
                # Используем строку вместо AttachmentType.ZIP для стабильности
                allure.attach.file(
                    trace_path,
                    name="Playwright_Trace",
                    attachment_type="application/zip"
                )
            else:
                page.context.tracing.stop()

            # Очистка
            page.context.clear_cookies()
            page.evaluate("window.localStorage.clear()")
            page.evaluate("window.sessionStorage.clear()")
        except (RuntimeError, KeyError, AttributeError):
            pass
    else:
        page.context.tracing.stop()


@pytest.fixture
def db_client():
    client = DbClient("test_database.db")
    # language=SQL
    create_table_sql = "CREATE TABLE IF NOT EXISTS test_logs (id INTEGER PRIMARY KEY, action TEXT, status TEXT)"
    client.execute_query(create_table_sql)
    yield client
    with allure.step("DB Cleanup: Removing test records"):
        client.execute_query("DELETE FROM test_logs")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_call", report)

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Failure_Screenshot",
                attachment_type=allure.attachment_type.PNG
            )