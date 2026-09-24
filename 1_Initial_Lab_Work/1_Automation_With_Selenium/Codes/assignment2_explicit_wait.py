from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

try:
    driver.get(
        "https://www.selenium.dev/selenium/web/dynamic.html"
    )
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Click the "Start" button
    start_button = wait.until(
        EC.element_to_be_clickable((By.ID, "adder"))
    )

    start_button.click()

    # Wait until the dynamically-created element appears
    result = wait.until(
        EC.presence_of_element_located(
            (By.ID, "box0")
        )
    )

    # Validate
    assert result.is_displayed()

    print("Assignment 2 PASSED")
    print("Dynamic element appeared successfully.")

finally:
    driver.quit()