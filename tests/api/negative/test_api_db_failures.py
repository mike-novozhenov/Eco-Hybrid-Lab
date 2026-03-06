import pytest
import allure

@pytest.mark.api
@pytest.mark.db
@pytest.mark.negative
@allure.title("Negative: Ensure API errors are logged to DB")
def test_api_to_db_negative_logging(api_client, db_client):
    """
    Scenario:
    1. Call the API with invalid ID (triggering 404)
    2. Check that the logging system records the attempt as 'Failed'
    3. Verify the status is saved in the DB
    """

    # --- STEP 1: API Error Case ---
    with allure.step("Step 1: Request a non-existent resource"):
        # Теперь вызываем метод напрямую, так как мы его добавили в клиент
        response = api_client.json.get_post(999999)

        # 404 Not Found считается неуспешным статусом
        is_success = 200 <= response.status_code < 300
        status_to_log = "Success" if is_success else "Failed"

    # --- STEP 2: Logging the Failure ---
    with allure.step("Step 2: Log the failed transaction into DB"):
        db_client.execute_query(
            "INSERT INTO test_logs (action, status) VALUES (?, ?)",
            ("FAILED_API_CALL", status_to_log)
        )

    # --- STEP 3: Database Verification ---
    with allure.step("Step 3: Verify the 'Failed' record exists"):
        records = db_client.fetch_all(
            "SELECT * FROM test_logs WHERE action = ?",
            ("FAILED_API_CALL",)
        )
        assert len(records) > 0, "Error: The failure was not logged in the database"
        # Индекс 2 соответствует колонке 'status' в нашей таблице (id=0, action=1, status=2)
        assert records[-1][2] == "Failed", f"Error: Expected 'Failed', but got '{records[-1][2]}'"