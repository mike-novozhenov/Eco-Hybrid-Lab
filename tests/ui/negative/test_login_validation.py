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
    home_page.open()
    login_page.open_modal()

    with home_page.page.expect_event("dialog") as dialog_info:
        with allure.step("Submit login with invalid credentials"):
            login_page.submit_login("unknown_user_999", "random_pass")

    dialog = dialog_info.value

    with allure.step("Verify alert text"):
        actual_message = dialog.message
        expected_error = "User does not exist."

        assert actual_message == expected_error, f"Expected '{expected_error}', but got '{actual_message}'"
        dialog.accept()
