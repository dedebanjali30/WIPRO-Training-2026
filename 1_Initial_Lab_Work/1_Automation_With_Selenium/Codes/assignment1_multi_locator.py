from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Username -> By.ID
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    # Password -> By.NAME
    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    # Login button -> By.XPATH
    login_button = driver.find_element(
        By.XPATH, "//input[@type='submit']"
    )
    login_button.click()

    # Validation
    assert "/inventory.html" in driver.current_url

    print("Assignment 1 PASSED")
    print("Current URL:", driver.current_url)

finally:
    driver.quit()