import pytest

# Mock data (in real life this comes from an API response)
@pytest.fixture
def job_post_data():
    return {
        "id": "fsd",
        "title": "QA Automation Engineer",
        "is_active": True
    }

def test_job_post_schema(job_post_data):
    """
    Validate the job_post object against the expected schema and business rules
    """
    schema = {
        "id": int,
        "title": str,
        "is_active": bool
    }

    # 1. Integrity check
    assert len(job_post_data) == len(schema), f"Expected {len(schema)} keys, but got {len(job_post_data)}"

    # 2. Type validation loop
    for key, expected_type in schema.items():
        assert key in job_post_data, f"Key '{key}' is missing in response"
        assert isinstance(job_post_data[key], expected_type), \
            f"Key '{key}' has wrong type: expected {expected_type.__name__}, got {type(job_post_data[key]).__name__}"

    # 3. Business logic validation
    assert job_post_data["title"] != "", "Job title should not be an empty string"
    assert job_post_data["id"] > 0, f"Expected positive ID, but got {job_post_data['id']}"