from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

print("Selenium started successfully")
print("Page Title:", driver.title)

driver.quit()