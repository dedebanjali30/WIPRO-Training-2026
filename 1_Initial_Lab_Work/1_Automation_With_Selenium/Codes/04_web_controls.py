from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

# Textbox
driver.find_element(By.ID, "name").send_keys("Debanjali")

# Radio button
driver.find_element(By.ID, "male").click()

# Checkbox
driver.find_element(By.ID, "sunday").click()

# Dropdown
Select(
    driver.find_element(By.ID, "country")
).select_by_visible_text("India")

print("Text box: PASS")
print("Radio button: PASS")
print("Checkbox: PASS")
print("Dropdown: PASS")

driver.quit()