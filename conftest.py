import os
import pytest
from dotenv import load_dotenv
from pages.product_page import ProductPage
from pages.cart_page import CartPage

# Load variables from .env file
load_dotenv()

@pytest.fixture
def product_page(page):
    """Fixture for Product Page Object initialization"""
    # Use environment variable for the base URL
    url = os.getenv("BASE_URL")
    page.goto(url)
    return ProductPage(page)

@pytest.fixture
def cart_page(page):
    """Fixture for Cart Page Object initialization"""
    return CartPage(page)