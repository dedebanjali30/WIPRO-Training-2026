from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import xml.etree.ElementTree as ET
import os


# ==========================================================
# 1. READ XML DATA
# ==========================================================

print("\n========== XML DATA ==========")

# Get the folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# XML file is in the same folder
xml_file = os.path.join(current_folder, "test_data.xml")

tree = ET.parse(xml_file)

root = tree.getroot()

for user in root:

    name = user.find("name").text
    email = user.find("email").text

    print("Name :", name)
    print("Email:", email)


# ==========================================================
# 2. OPEN WEBSITE
# ==========================================================

print("\n========== SELENIUM ==========")

driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "https://testautomationpractice.blogspot.com/"
)

print("Website opened successfully")


# ==========================================================
# 3. MOUSE HOVER
# ==========================================================

print("\n========== MOUSE HOVER ==========")

try:

    hover_element = driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Point Me')]"
    )

    ActionChains(driver).move_to_element(
        hover_element
    ).perform()

    print("Mouse hover performed successfully")

except Exception as e:

    print("Mouse hover error:", e)


# ==========================================================
# 4. JAVASCRIPT COMMAND
# ==========================================================

print("\n========== JAVASCRIPT ==========")

try:

    driver.execute_script(
        "window.scrollTo(0, 500);"
    )

    print("JavaScript executed successfully")

except Exception as e:

    print("JavaScript error:", e)


# ==========================================================
# 5. EXCEPTION HANDLING
# ==========================================================

print("\n========== EXCEPTION HANDLING ==========")

try:

    driver.find_element(
        By.ID,
        "wrong_element_id"
    )

except Exception:

    print("Exception handled successfully")

finally:

    print("Finally block executed")


# ==========================================================
# 6. CLOSE BROWSER
# ==========================================================

driver.quit()

print("\nBrowser closed successfully")

print("\n========== PROGRAM COMPLETED ==========")