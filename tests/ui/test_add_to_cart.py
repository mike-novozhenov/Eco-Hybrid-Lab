import pytest
import allure

@pytest.mark.ui  # Adding the UI tag
@allure.title("Test Case 1: Pure UI - Add Product to Cart")
def test_add_samsung_to_cart(product_page, cart_page): # Теперь передаем фикстуры страниц напрямую
    target_product = "Samsung galaxy s6"

    with allure.step(f"Open product page for {target_product}"):
        product_page.navigate("prod.html?idp_=1")

    with allure.step("Add product to cart and handle alert"):
        product_page.add_to_cart()

    with allure.step("Verify product in cart"):
        cart_page.open_cart()
        assert cart_page.is_product_in_cart(target_product)