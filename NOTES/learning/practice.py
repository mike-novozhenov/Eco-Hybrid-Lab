# job_post = {
#     "id": 105,
#     "title": "QA Automation Engineer",
#     "is_active": True
# }
#
# # Твой код здесь:
# assert isinstance(job_post["id"], int)
# assert isinstance(job_post["title"], str)
# assert job_post["title"] != ""
# # ---
#
# candidates = [
#     {"name": "Mikhail", "email": "mihail@test.com"},
#     {"name": "Ivan", "email": None},
#     {"name": "Alex", "email": "alex@test.com"}
# ]
#
# # Твой код здесь (используй isinstance или просто проверку на None):
# for i in candidates:
#     assert i["email"] is not None, f"Candidate {i['name']} has email = None"
#     assert i["email"] != "", f"Candidate {i['name']} has no email"
#
#
# # ---
#
# tags = ["Python", "Pytest", "Playwright", "API"]
#
# # Твой код здесь:
# assert len(tags) > 2
# assert tags[0] == "Python"

import pytest
import requests  # Библиотека для API запросов


@pytest.fixture
def candidate_id():
    # SETUP: Реальный запрос к серверу АТС на создание
    response = requests.post("https://ats.com/api/candidates", data={"name": "Mikhail"})
    c_id = response.json()["id"]

    yield c_id  # ТУТ ПАУЗА. Идет выполнение теста.

    # TEARDOWN: Реальный запрос на удаление.
    # Он выполнится, даже если тест ВЫШЕ провалился.
    requests.delete(f"https://ats.com/api/candidates/{c_id}")
    print(f"CLEANED UP: Candidate {c_id} deleted")


import pytest

@pytest.fixture
def candidate_id():
    print("\n[STEP 1] Setup: Creating candidate...")
    yield 12345
    print("\n[STEP 3] Teardown: Deleting candidate...")

def test_hiring_process(candidate_id):
    print(f"[STEP 2] Running test with ID: {candidate_id}")
    # Специально валим тест:
    assert 1 == 2


