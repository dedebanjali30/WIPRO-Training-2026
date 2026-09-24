from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.save_screenshot(
    "automation_page.png"
)

print("Screenshot captured successfully")

driver.quit()