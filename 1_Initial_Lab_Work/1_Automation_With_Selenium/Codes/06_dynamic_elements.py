from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

rows = driver.find_elements(
    By.XPATH,
    "//table[@name='BookTable']//tr"
)

print("Total Rows:", len(rows))

for row in rows:
    print(row.text)

driver.quit()