from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    SEARCH = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")

    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//h2[contains(translate(., "
        "'abcdefghijklmnopqrstuvwxyz', "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), "
        "'SEARCHED PRODUCTS')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def wait_for_products_page(self):

        # Wait for page loading to complete
        self.wait.until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Wait for the search box
        self.wait.until(
            EC.presence_of_element_located(
                self.SEARCH
            )
        )

    def search_product(self, product):

        self.wait_for_products_page()

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH
            )
        )

        field.clear()
        field.send_keys(product)

        search_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        )

        search_button.click()

    def search_results_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCHED_PRODUCTS
            )
        ).is_displayed()

    def open_product(self, product_name):

        card = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@class,'product-image-wrapper')]"
                    f"[.//p[normalize-space()='{product_name}']]"
                )
            )
        )

        view_product = card.find_element(
            By.XPATH,
            ".//a[contains(normalize-space(.), 'View Product')]"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            view_product
        )

        self.wait.until(
            EC.element_to_be_clickable(view_product)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            view_product
        )