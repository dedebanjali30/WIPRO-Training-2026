from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Simple Alert')]"
).click()

alert = driver.switch_to.alert

print("Alert Text:", alert.text)

alert.accept()

print("Alert handled successfully")

driver.quit()