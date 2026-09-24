from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "name").send_keys("Debanjali")

driver.find_element(
    By.XPATH,
    "//input[@id='email']"
).send_keys("test@gmail.com")

driver.find_element(
    By.CSS_SELECTOR,
    "#phone"
).send_keys("9876543210")

print("Locators executed successfully")

driver.quit()