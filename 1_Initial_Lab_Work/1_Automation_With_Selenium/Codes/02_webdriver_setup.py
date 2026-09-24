from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

print("Browser:", driver.name)
print("Title:", driver.title)
print("URL:", driver.current_url)

driver.quit()