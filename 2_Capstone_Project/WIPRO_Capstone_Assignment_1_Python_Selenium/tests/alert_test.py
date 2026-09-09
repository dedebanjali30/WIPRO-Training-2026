
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


# Add project root to Python path
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)


def main():

    # ============================================
    # START BROWSER
    # ============================================

    options = Options()

    options.add_argument(
        "--start-maximized"
    )

    options.add_argument(
        "--disable-notifications"
    )

    driver = webdriver.Chrome(
        options=options
    )

    wait = WebDriverWait(
        driver,
        10
    )

    try:

        # ============================================
        # OPEN DEMO WEBSITE
        # ============================================

        driver.get(
            "https://testautomationpractice.blogspot.com/"
        )

        print()
        print("========================================")
        print("SELENIUM ALERT HANDLING TEST")
        print("========================================")

        # ============================================
        # CREATE JAVASCRIPT ALERT
        # ============================================

        driver.execute_script(
            "alert('Wipro Selenium Alert Test');"
        )

        # ============================================
        # HANDLE ALERT
        # ============================================

        alert = wait.until(
            lambda d: d.switch_to.alert
        )

        alert_text = alert.text

        print(
            "Alert message:",
            alert_text
        )

        # Accept alert
        alert.accept()

        print(
            "Alert accepted successfully ✅"
        )

        # ============================================
        # VERIFY ALERT WAS CLOSED
        # ============================================

        try:

            wait.until(
                lambda d: d.switch_to.alert
            )

            print(
                "Alert was still present ❌"
            )

        except Exception:

            print(
                "Alert closed successfully ✅"
            )

        print()
        print("========================================")
        print("ALERT TEST PASSED ✅")
        print("========================================")

    except Exception as error:

        print()
        print("========================================")
        print("ALERT TEST FAILED ❌")
        print("========================================")

        print(
            "Error:",
            error
        )

        print("========================================")

        raise

    finally:

        driver.quit()


if __name__ == "__main__":
    main()

