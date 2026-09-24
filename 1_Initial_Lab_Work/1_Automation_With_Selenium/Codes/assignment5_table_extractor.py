from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

try:
    driver.get("https://the-internet.herokuapp.com/tables")
    driver.maximize_window()

    # Locate first table
    table = driver.find_element(By.ID, "table1")

    # Get all rows
    rows = table.find_elements(By.TAG_NAME, "tr")

    search_name = "Smith"

    found = False

    for row in rows[1:]:  # Skip header
        columns = row.find_elements(By.TAG_NAME, "td")

        if not columns:
            continue

        # Table columns:
        # Last Name | First Name | Email | Due | Web Site | Action

        last_name = columns[0].text
        due = columns[3].text

        if last_name == search_name:
            print("Name:", last_name)
            print("Due/Price:", due)

            found = True
            break

    assert found, f"{search_name} not found in table"

    print("Assignment 5 PASSED")

finally:
    driver.quit()