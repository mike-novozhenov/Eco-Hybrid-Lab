import requests
import allure

class JsonPlaceholderApi:
    """Methods for interacting with the JSONPlaceholder service"""

    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("API: Create a new resource (POST)")
    def create_post(self, payload: dict):
        url = f"{self.base_url}/posts"
        return requests.post(url, json=payload, timeout=10)

    @allure.step("API: Get resource by ID (GET)")
    def get_post(self, post_id: int):
        url = f"{self.base_url}/posts/{post_id}"
        return requests.get(url, timeout=10)


class ApiClient:
    """Main entry point for API services (Wrapper)"""

    def __init__(self):
        # Инициализируем сессию для переиспользования соединений
        self.session = requests.Session()
        # Оставляем поддержку существующего сервиса
        self.json = JsonPlaceholderApi("https://jsonplaceholder.typicode.com")

    @allure.step("API: Universal GET request")
    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    @allure.step("API: Universal HEAD request")
    def head(self, url, **kwargs):
        return self.session.head(url, **kwargs)

    @allure.step("API: Universal POST request")
    def post(self, url, **kwargs):
        return self.session.post(url, **kwargs)