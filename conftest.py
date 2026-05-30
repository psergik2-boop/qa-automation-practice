"""
Shared fixtures for the entire test suite.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# ─── API fixtures ────────────────────────────────────────────────────────────

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_base_url():
    return BASE_URL


# ─── UI fixtures ─────────────────────────────────────────────────────────────

@pytest.fixture
def driver():
    """Setup and teardown for Chrome browser."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")          # запуск без окна (CI-friendly)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Driver already logged in as standard_user."""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver
