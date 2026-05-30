"""
UI tests for SauceDemo.
Demo e-commerce site for practising UI automation skills.
URL: https://www.saucedemo.com
"""

from selenium.webdriver.common.by import By


def test_successful_login(logged_in_driver):
    """User should be able to log in with valid credentials."""
    assert "inventory" in logged_in_driver.current_url


def test_login_with_locked_user(driver):
    """A locked-out user should see an error message."""
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "locked" in error.text.lower()


def test_login_with_empty_fields(driver):
    """Empty fields should show a validation error."""
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username is required" in error.text


def test_add_product_to_cart(logged_in_driver):
    """User should be able to add a product to the cart."""
    logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    cart_badge = logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"
