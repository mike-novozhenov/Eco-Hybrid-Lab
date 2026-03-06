import sqlite3
import allure

class DbClient:
    def __init__(self, db_path="test_database.db"):
        self.db_path = db_path

    @allure.step("DB: Execute query")
    def execute_query(self, query, params=()):
        """Executes a query (INSERT, UPDATE, DELETE)"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    @allure.step("DB: Fetch data")
    def fetch_all(self, query, params=()):
        """Fetches data from the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()