
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
from pages.product_page import ProductPage
from pages.cart_page import CartPage

from utils.config import load_test_data, load_credentials
from utils.screenshot import take_screenshot
from utils.report import ExecutionReport


def main():

    # =================================================
    # LOAD DATA
    # =================================================

    data = load_test_data()
    credentials = load_credentials()

    report = ExecutionReport()

    # =================================================
    # CHROME OPTIONS
    # =================================================

    options = Options()

    options.add_argument(
        "--start-maximized"
    )

    options.add_argument(
        "--disable-notifications"
    )

    # =================================================
    # START BROWSER
    # =================================================

    driver = webdriver.Chrome(
        options=options
    )

    wait = WebDriverWait(
        driver,
        30
    )

    try:

        # =================================================
        # STEP 1 - OPEN WEBSITE
        # =================================================

        driver.get(
            data["base_url"]
        )

        wait.until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        print()
        print("Website opened ✅")

        take_screenshot(
            driver,
            "01_home_page"
        )

        # =================================================
        # STEP 2 - OPEN LOGIN
        # =================================================

        login_link = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "a[href='/login']"
                )
            )
        )

        login_link.click()

        login = LoginPage(driver)

        assert login.is_login_page_displayed(), \
            "Login page was not displayed"

        # =================================================
        # STEP 3 - LOGIN
        # =================================================

        login.login(
            credentials["email"],
            credentials["password"]
        )

        assert login.is_logged_in(), \
            "Login was not successful"

        print("Login successful ✅")

        take_screenshot(
            driver,
            "02_logged_in"
        )

        # =================================================
        # STEP 4 - CLEAN CART BEFORE TEST
        # =================================================

        driver.get(
            data["base_url"] + "/view_cart"
        )

        cart = CartPage(driver)

        for test_case in data["positive_tests"]:

            product = test_case["product"]

            if cart.product_exists(product):

                print(
                    f"Removing old {product} from cart..."
                )

                cart.remove_product(product)

        print("Cart ready for testing ✅")

        # =================================================
        # STEP 5 - ADD ALL PRODUCTS TO CART
        # =================================================

        print()
        print("========================================")
        print("ADDING PRODUCTS TO CART")
        print("========================================")

        for index, test_case in enumerate(
            data["positive_tests"],
            start=1
        ):

            product = test_case["product"]
            quantity = test_case["quantity"]

            print()
            print(
                f"PRODUCT {index}: {product}"
            )
            print(
                f"Quantity: {quantity}"
            )

            # Open products page
            driver.get(
                data["base_url"] + "/products"
            )

            products = ProductsPage(driver)

            products.wait_for_products_page()

            # Search product
            products.search_product(
                product
            )

            assert products.search_results_displayed(), \
                f"Search results not displayed for {product}"

            print(
                f"{product} search successful ✅"
            )

            # Open product
            products.open_product(
                product
            )

            product_page = ProductPage(driver)

            assert product_page.is_product_page_displayed(), \
                f"Product page not displayed for {product}"

            print(
                f"{product} opened ✅"
            )

            # Set quantity
            product_page.set_quantity(
                quantity
            )

            print(
                f"Quantity set to {quantity} ✅"
            )

            # Add product
            product_page.add_to_cart()

            print(
                f"{product} added to cart ✅"
            )

        # =================================================
        # STEP 6 - OPEN CART
        # =================================================

        product_page.click_view_cart()

        cart = CartPage(driver)

        assert cart.is_cart_displayed(), \
            "Shopping cart was not displayed"

        print()
        print("========================================")
        print("SHOPPING CART")
        print("========================================")

        print(
            "All products added to cart successfully ✅"
        )

        # =================================================
        # STEP 7 - VERIFY ALL PRODUCTS
        # =================================================

        for test_case in data["positive_tests"]:

            product = test_case["product"]
            expected_quantity = test_case["quantity"]

            # Verify product exists
            assert cart.product_exists(product), \
                f"{product} was not found in cart"

            # Verify quantity
            actual_quantity = cart.get_quantity(
                product
            )

            assert actual_quantity == str(expected_quantity), \
                f"{product}: Expected quantity {expected_quantity}, got {actual_quantity}"

            # Get price
            price = cart.get_price(
                product
            )

            # Get total
            total = cart.get_total(
                product
            )

            print()
            print(
                f"Product : {product}"
            )
            print(
                f"Quantity: {actual_quantity} ✅"
            )
            print(
                f"Price   : {price} ✅"
            )
            print(
                f"Total   : {total} ✅"
            )

        # =================================================
        # STEP 8 - CART SCREENSHOT
        # =================================================

        take_screenshot(
            driver,
            "03_all_products_cart"
        )

        # =================================================
        # STEP 9 - FINAL RESULT
        # =================================================

        report.add(
            "All positive product tests",
            "PASS",
            f"{len(data['positive_tests'])} products added and verified together"
        )

        print()
        print("========================================")
        print("ALL POSITIVE TESTS PASSED ✅")
        print("========================================")
        print(
            f"Products tested: {len(data['positive_tests'])}"
        )
        print(
            "All products are present together in the cart ✅"
        )
        print("========================================")

    except Exception as error:

        report.add(
            "Positive test execution",
            "FAIL",
            str(error)
        )

        try:

            take_screenshot(
                driver,
                "FAILED_POSITIVE_TEST"
            )

        except Exception:
            pass

        print()
        print("========================================")
        print("POSITIVE TEST EXECUTION FAILED")
        print("========================================")
        print(
            "Error:",
            error
        )
        print("========================================")

        raise

    finally:

        # =================================================
        # SAVE REPORT
        # =================================================

        report_path = report.save()

        print()
        print(
            "Execution report:",
            report_path
        )

        # =================================================
        # CLOSE BROWSER
        # =================================================

        driver.quit()


if __name__ == "__main__":
    main()
