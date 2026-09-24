from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://testautomationpractice.blogspot.com/")

    wait = WebDriverWait(driver, 10)

    # -------------------------------
    # CHECKBOXES
    # -------------------------------

    checkboxes = driver.find_elements(
        By.CSS_SELECTOR,
        "input[type='checkbox']"
    )

    print("Total checkboxes:", len(checkboxes))

    # Select first two unchecked checkboxes
    selected = 0

    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
            selected += 1

        if selected == 2:
            break

    print("Two checkboxes selected successfully")

    # Verify selected state
    for checkbox in checkboxes[:2]:
        print("Selected:", checkbox.is_selected())

    # -------------------------------
    # DYNAMIC / AUTOCOMPLETE DROPDOWN
    # -------------------------------

    country_input = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "autocomplete")
        )
    )

    country_input.send_keys("Ind")

    suggestions = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".ui-menu-item")
        )
    )

    print("Suggestions found:", len(suggestions))

    for suggestion in suggestions:
        text = suggestion.text

        print("Suggestion:", text)

        if "India" in text:
            suggestion.click()
            print("India selected successfully")
            break

    print("ASSIGNMENT 3 PASSED")

finally:
    driver.quit()