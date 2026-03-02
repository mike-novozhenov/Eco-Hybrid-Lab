# API
@pytest.fixture
def job_post_data():
    import requests
    response = requests.get("https://api.example.com/jobs/105")
    return response.json()

# ---

# JSON/CSV
@pytest.fixture
def job_post_data():
    import json
    with open("job.json") as f:
        return json.load(f)

