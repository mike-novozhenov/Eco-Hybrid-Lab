import pytest
import allure
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.negative
@allure.epic("UI Resilience")
@allure.feature("Auth Validation")
@allure.title("Negative: Error message for non-existent user")
def test_login_user_not_found(home_page, login_page: LoginPage):
    """
    Test verifies that an alert appears with 'User does not exist.'
    using dynamic event waiting instead of static timeouts.
    """
    # 1. Setup
    home_page.open()
    login_page.open_modal()

    # 2. Action & Event Catching
    # Ожидаем событие диалога (алерта) параллельно с кликом
    with home_page.page.expect_event("dialog") as dialog_info:
        with allure.step("Submit login with invalid credentials"):
            login_page.submit_login("unknown_user_999", "random_pass")

    # 3. Verification
    # dialog_info.value — это объект диалога, который мы поймали
    dialog = dialog_info.value

    with allure.step("Verify alert text"):
        actual_message = dialog.message
        expected_error = "User does not exist."

        # Сначала проверяем текст, затем закрываем (accept)
        assert actual_message == expected_error, f"Expected '{expected_error}', but got '{actual_message}'"
        dialog.accept()