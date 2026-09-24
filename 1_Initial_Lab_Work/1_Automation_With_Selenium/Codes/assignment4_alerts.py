from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    # -------------------------------
    # 1. JavaScript Alert
    # -------------------------------
    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Alert']"
    ).click()

    alert = wait.until(lambda d: d.switch_to.alert)

    print("Alert text:", alert.text)

    alert.accept()

    # -------------------------------
    # 2. Confirm Box
    # -------------------------------
    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Confirm']"
    ).click()

    alert = wait.until(lambda d: d.switch_to.alert)

    print("Confirm text:", alert.text)

    # Dismiss the confirm box
    alert.dismiss()

    # -------------------------------
    # 3. Prompt Box
    # -------------------------------
    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Prompt']"
    ).click()

    alert = wait.until(lambda d: d.switch_to.alert)

    print("Prompt text:", alert.text)

    # Send text to prompt
    alert.send_keys("[1, 2, 3, 4]")

    # Accept prompt
    alert.accept()

    print("Assignment 4 PASSED")

finally:
    driver.quit()