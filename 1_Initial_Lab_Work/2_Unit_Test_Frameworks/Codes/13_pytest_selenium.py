import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_selenium_form(driver):

    driver.get(
        "https://testautomationpractice.blogspot.com/"
    )

    name = driver.find_element(By.ID, "name")
    email = driver.find_element(By.ID, "email")

    name.send_keys("Debanjali")
    email.send_keys("debanjali@gmail.com")

    assert name.is_displayed()
    assert email.is_displayed()