job_post = {
    "id": 105,
    "title": "QA Automation Engineer",
    "is_active": True
}

# Define expected types for validation
# This schema serves as a 'Contract' for the API response
schema = {
    "id": int,
    "title": str,
    "is_active": bool
}

# 1. Check for unexpected extra keys (Strict validation)
assert len(job_post) == len(schema), f"Payload size mismatch: expected {len(schema)} keys"

# 2. Iterate through the schema to validate the job_post
for key, expected_type in schema.items():
    # Check if key exists
    assert key in job_post, f"Missing key: {key}"
    # Check value type
    assert isinstance(job_post[key], expected_type), f"Wrong type for key '{key}'"

# 3. Additional business logic checks (Post-schema validation)
assert job_post["title"] != "", "Title should not be empty"