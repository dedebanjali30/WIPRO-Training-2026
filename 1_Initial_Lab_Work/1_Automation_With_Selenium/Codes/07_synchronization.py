from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

# Implicit Wait
driver.implicitly_wait(5)

driver.find_element(
    By.ID, "name"
).send_keys("Debanjali")

print("Implicit Wait: PASS")

# Explicit Wait
wait = WebDriverWait(driver, 10)

email = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "email")
    )
)

email.send_keys("test@gmail.com")

print("Explicit Wait: PASS")

driver.quit()