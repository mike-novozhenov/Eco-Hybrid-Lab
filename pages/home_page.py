class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.demoblaze.com/index.html"

    def open(self):
        self.page.goto(self.url)
        # Небольшое ожидание, чтобы страница не была "голой" при сборе ссылок
        self.page.wait_for_load_state("networkidle")