from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

wait = WebDriverWait(driver, 10)

try:

    # ==================================================
    # PART 1 — IFRAME
    # ==================================================

    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.maximize_window()

    print("Iframe page opened")

    # Wait for iframe
    iframe = wait.until(
        EC.presence_of_element_located(
            (By.ID, "mce_0_ifr")
        )
    )

    # Switch into iframe
    driver.switch_to.frame(iframe)

    print("Switched into iframe")

    # Locate editor
    editor = wait.until(
        EC.presence_of_element_located(
            (By.ID, "tinymce")
        )
    )

    # Clear content using keyboard
    editor.click()
    editor.send_keys(Keys.CONTROL, "a")
    editor.send_keys("Hello from Selenium!")

    print("Text entered inside iframe")

    # Switch back to main page
    driver.switch_to.default_content()

    print("Switched back to main page")


    # ==================================================
    # PART 2 — NEW TAB / WINDOW
    # ==================================================

    driver.get("https://the-internet.herokuapp.com/windows")

    original_window = driver.current_window_handle

    print("Original window:", original_window)

    # Click link
    driver.find_element(
        By.LINK_TEXT, "Click Here"
    ).click()

    # Wait for second window
    wait.until(
        lambda d: len(d.window_handles) == 2
    )

    # Switch to new window
    for window in driver.window_handles:

        if window != original_window:
            driver.switch_to.window(window)
            break

    print("New window opened")
    print("New window title:", driver.title)

    # Close new window
    driver.close()

    print("New window closed")

    # Switch back to original window
    driver.switch_to.window(original_window)

    print("Returned to original window")
    print("Main page title:", driver.title)

    print("================================")
    print("ASSIGNMENT 6 PASSED")
    print("================================")


finally:
    driver.quit()