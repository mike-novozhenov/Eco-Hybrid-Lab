# 📋 Test Cases Specification

## Test Case 1: Pure UI - Add Product to Cart (site: [Demoblaze](https://www.demoblaze.com/))
(**Test name: test_add_to_cart.py**)

### 📝 Description
Verification of basic e-commerce functionality: selecting a product, interacting with browser-native dialogs (Alerts), and ensuring cart persistence via **UI**

### 🏗 Pre-conditions
* Environment: Production/Staging URL access authorized
* Browser Context: Default Playwright session (incognito-like)
* Test Data: At least one product must be available in the "Phones" category

### 👣 Steps
1. Navigate to the [Demoblaze](https://www.demoblaze.com/) home page
2. Select the "Phones" category from the side menu
3. Click on the first available product (e.g., "Samsung galaxy s6")
4. Click the "Add to cart" button on the product detail page
5. Wait for the browser modal (Alert) with the text "Product added" to appear
6. Click "OK" on the alert dialog
7. Navigate to the "Cart" section via the top navigation bar

### ✅ Expected Result
* The cart table displays exactly one row with the selected item
* Product name, price, and the "Delete" button match the chosen item
* The "Total" amount is calculated correctly based on the product price