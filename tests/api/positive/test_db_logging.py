import pytest
import allure


@pytest.mark.api
@pytest.mark.db
@allure.title("Database: Log API results to SQL table and Verify")
def test_api_to_db_logging(api_client, db_client):
    """
    Scenario:
    1. Call the API to create a resource (POST)
    2. Save the operation result into SQLite database (INSERT)
    3. Verify the record exists in the DB (SELECT)
    4. Cleanup is handled automatically by the db_client fixture (Teardown)
    """
    title = "DB Integration Test"

    # --- STEP 1: Interaction with API ---
    with allure.step("Step 1: Create resource via API"):
        response = api_client.json.create_post({"title": title, "body": "Testing DB", "userId": 1})
        status_to_log = "Success" if response.status_code == 201 else "Failed"

    # --- STEP 2: SQL INSERT Operation ---
    with allure.step("Step 2: Log action into Database (INSERT)"):
        db_client.execute_query(
            "INSERT INTO test_logs (action, status) VALUES (?, ?)", (f"Create post: {title}", status_to_log)
        )

    # --- STEP 3: SQL SELECT & Validation ---
    with allure.step("Step 3: Verify record in DB (SELECT)"):
        records = db_client.fetch_all("SELECT * FROM test_logs WHERE action = ?", (f"Create post: {title}",))

        assert len(records) > 0, f"Error: No records found for title '{title}'"

        allure.attach(
            str(records[-1]), name="Database Verification Result", attachment_type=allure.attachment_type.TEXT
        )
