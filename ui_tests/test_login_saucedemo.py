"""
UI tests for SauceDemo website
A demo e-commerce website for practicing UI automation.
URL: https://www.saucedemo.com
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    """Setup and teardown for browser"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()


def test_successful_login(driver):
    """User should be able to login with valid credentials"""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url


def test_login_with_locked_user(driver):
    """Locked out user should see error message"""
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "locked out" in error.text.lower()


def test_login_with_empty_fields(driver):
    """Empty fields should show validation error"""
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username is required" in error.text


def test_add_product_to_cart(driver):
    """User should be able to add product to cart"""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"
