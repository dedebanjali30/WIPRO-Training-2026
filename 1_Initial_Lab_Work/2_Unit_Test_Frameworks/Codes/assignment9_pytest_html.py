import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.test_failed = report.failed


@pytest.fixture
def driver(request):

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    if getattr(request.node, "test_failed", False):

        os.makedirs("Screenshots", exist_ok=True)

        screenshot_name = os.path.join(
            "Screenshots",
            request.node.name + "_FAILED.png"
        )

        driver.save_screenshot(screenshot_name)

        print(
            f"\nFailure screenshot saved: "
            f"{screenshot_name}"
        )

    driver.quit()


def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys("standard_user")

    driver.find_element(
        By.ID,
        "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID,
        "login-button"
    ).click()

    assert "inventory.html" in driver.current_url


def test_page_title(driver):

    driver.get("https://www.saucedemo.com/")

    assert "Swag Labs" in driver.title