import pytest
import allure


@pytest.mark.api
@pytest.mark.smoke
@allure.title("Positive: Create resource and verify data contract")
def test_create_resource_positive(api_client):
    """
    Standard positive scenario:
    1. HTTP Status 201
    2. Header Content-Type is JSON
    3. Response Body types validation
    """
    payload = {"title": "Advanced QA Architecture", "body": "Checking types and headers for portfolio", "userId": 1}

    with allure.step("Send POST request via ApiClient"):
        response = api_client.json.create_post(payload)
        data = response.json()

    with allure.step("Verify HTTP Contract (Status & Headers)"):
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        assert "application/json" in response.headers["Content-Type"]

    with allure.step("Verify Data Schema and Types"):
        assert isinstance(data["id"], int), "Server must return ID as an integer"
        assert data["title"] == payload["title"]
        assert data["userId"] == payload["userId"]

    with allure.step("Attach response for report"):
        allure.attach(str(data), name="Backend Response JSON", attachment_type=allure.attachment_type.JSON)


@pytest.mark.api
@allure.title("Negative: Create resource with invalid data types")
def test_create_resource_negative_types(api_client):
    """
    Negative scenario:
    - Sending 'None' and invalid types
    - Verifying server stability and error handling
    """
    payload = {
        "title": None,
        "body": 12345,
        "userId": "not-an-id",
    }

    with allure.step("Send POST request with invalid payload"):
        response = api_client.json.create_post(payload)
        data = response.json()

    with allure.step("Verify server stability"):
        assert response.status_code in [201, 400], f"Unexpected status code: {response.status_code}"

    with allure.step("Log server behavior for invalid data"):
        allure.attach(str(data), name="Server reaction to invalid data", attachment_type=allure.attachment_type.JSON)
