import pytest


# Представим, что эта фикстура живет в conftest.py
@pytest.fixture
def job_post_data():
    # --- SETUP: Создание данных ---
    print("\n[Setup] Connecting to ATS API and creating a job...")

    # В реальности тут был бы запрос к серверу.
    # Специально оставим "id": "fsd" (строку), чтобы увидеть, как сработает Teardown при падении.
    payload = {
        "id": "---!!!SMTH WRONG!!! ---",
        "title": "QA Automation Engineer",
        "is_active": True
    }

    yield payload  # <--- ПЕРЕДАЧА ДАННЫХ В ТЕСТ

    # --- TEARDOWN: Очистка данных ---
    # Этот код выполнится ДАЖЕ ЕСЛИ тест ниже упадет
    print(f"\n[Teardown] Sending DELETE request to API for job ID: {payload.get('id')}")
    print("[Teardown] Database is clean now.")


def test_job_post_schema(job_post_data):
    """
    Validate the job_post object against the expected schema and business rules
    """
    # Твоя схема (Contract)
    schema = {
        "id": int,
        "title": str,
        "is_active": bool
    }

    # 1. Integrity check (Количество ключей)
    assert len(job_post_data) == len(schema), \
        f"Expected {len(schema)} keys, but got {len(job_post_data)}"

    # 2. Type validation loop (Твой цикл проверки типов)
    for key, expected_type in schema.items():
        # Проверяем, что ключ вообще пришел
        assert key in job_post_data, f"Key '{key}' is missing in response"

        # Проверяем тип данных (isinstance)
        # Твой тест упадет здесь, так как "fsd" (str) != int
        assert isinstance(job_post_data[key], expected_type), \
            f"Key '{key}' has wrong type: expected {expected_type.__name__}, got {type(job_post_data[key]).__name__}"

    # 3. Business logic validation (Дополнительные проверки)
    assert job_post_data["title"] != "", "Job title should not be an empty string"

    # Если id был бы числом, мы бы проверили, что он положительный
    if isinstance(job_post_data["id"], int):
        assert job_post_data["id"] > 0, f"Expected positive ID, but got {job_post_data['id']}"

class Calculator:
    num = 100

