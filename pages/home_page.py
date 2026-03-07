class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.demoblaze.com/index.html"

    def open(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
