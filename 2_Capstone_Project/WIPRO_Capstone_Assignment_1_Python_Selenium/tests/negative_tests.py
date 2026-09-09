import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

from utils.config import load_test_data
from utils.screenshot import take_screenshot


def invalid_login_test():

    data = load_test_data()

    credentials = data["negative_tests"]["invalid_login"]

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 30)

    try:

        print()
        print("========================================")
        print("NEGATIVE TEST 1 - INVALID LOGIN")
        print("========================================")

        driver.get(
            data["base_url"] + "/login"
        )

        login = LoginPage(driver)

        login.login(
            credentials["email"],
            credentials["password"]
        )

        error = login.get_login_error()

        assert "incorrect" in error.lower()

        print("Invalid login correctly rejected ✅")
        print("Error:", error)

        take_screenshot(
            driver,
            "negative_invalid_login"
        )

        print("TEST PASSED ✅")

    finally:

        driver.quit()


def invalid_product_test():

    data = load_test_data()

    invalid_product = data["negative_tests"]["invalid_product"]

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 30)

    try:

        print()
        print("========================================")
        print("NEGATIVE TEST 2 - INVALID PRODUCT")
        print("========================================")

        driver.get(
            data["base_url"] + "/products"
        )

        products = ProductsPage(driver)

        products.search_product(
            invalid_product
        )

        # Wait for search result section
        products.search_results_displayed()

        # Check that the invalid product does not exist
        product_found = driver.find_elements(
            By.XPATH,
            f"//p[normalize-space()='{invalid_product}']"
        )

        assert len(product_found) == 0

        print(
            f"Product '{invalid_product}' was not found ✅"
        )

        take_screenshot(
            driver,
            "negative_invalid_product"
        )

        print("TEST PASSED ✅")

    finally:

        driver.quit()


if __name__ == "__main__":

    invalid_login_test()

    invalid_product_test()

    print()
    print("========================================")
    print("ALL NEGATIVE TESTS PASSED")
    print("========================================")