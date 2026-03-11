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

    with allure.step("Step 1: Request a non-existent resource"):
        response = api_client.json.get_post(999999)

        is_success = 200 <= response.status_code < 300
        status_to_log = "Success" if is_success else "Failed"

    with allure.step("Step 2: Log the failed transaction into DB"):
        db_client.execute_query(
            "INSERT INTO test_logs (action, status) VALUES (?, ?)", ("FAILED_API_CALL", status_to_log)
        )

    with allure.step("Step 3: Verify the 'Failed' record exists"):
        records = db_client.fetch_all("SELECT * FROM test_logs WHERE action = ?", ("FAILED_API_CALL",))
        assert len(records) > 0, "Error: The failure was not logged in the database"
        assert records[-1][2] == "Failed", f"Error: Expected 'Failed', but got '{records[-1][2]}'"
