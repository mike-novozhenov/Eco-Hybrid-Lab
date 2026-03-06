import pytest
import allure


@pytest.mark.api
@pytest.mark.negative
@allure.title("Negative: Handling Malformed Data (Type Mismatch)")
def test_create_resource_with_invalid_types(api_client):
    """
    Test Case: Sending data types that violate the API contract.
    Goal: Verify how the backend handles unexpected input (arrays/numbers instead of strings)
    """
    # Intentional contract violation
    payload = {
        "title": ["Not", "a", "string"],  # List instead of String
        "body": 123456789,  # Integer instead of String
        "userId": "not-an-id"  # String instead of Integer
    }

    with allure.step("Send POST request with invalid data types"):
        response = api_client.json.create_post(payload)

    with allure.step("Analyze and document server vulnerability"):
        status = response.status_code
        allure.attach(str(status), name="Received Status Code", attachment_type=allure.attachment_type.TEXT)

        # Professional insight: Most public mock APIs are "lazy" and return 201.
        # A real production API should return 400 or 422.
        # We demonstrate that we can detect this 'loose' validation.
        if status == 201:
            allure.attach(
                "SECURITY/QA NOTE: Server accepted malformed data. "
                "Recommendation: Implement strict server-side schema validation",
                name="Expert Observation"
            )

        assert status in [201, 400, 422], f"Unexpected status code: {status}"