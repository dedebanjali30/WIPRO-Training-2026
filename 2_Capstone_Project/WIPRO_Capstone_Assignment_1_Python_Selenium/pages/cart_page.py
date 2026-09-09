from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_HEADING = (
        By.XPATH,
        "//li[contains(@class,'active') and contains(., 'Shopping Cart')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_cart_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.CART_HEADING
            )
        ).is_displayed()

    def get_product_row(self, product):

        xpath = (
            "//tr[.//td[contains(@class,'cart_description')]"
            "//a[normalize-space()=" + repr(product) + "]]"
        )

        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath)
            )
        )

    def product_exists(self, product):

        try:
            return self.get_product_row(product).is_displayed()

        except Exception:
            return False

    def get_quantity(self, product):

        return self.get_product_row(product).find_element(
            By.CSS_SELECTOR,
            "td.cart_quantity"
        ).text.strip()

    def get_price(self, product):

        return self.get_product_row(product).find_element(
            By.CSS_SELECTOR,
            "td.cart_price"
        ).text.strip()

    def get_total(self, product):

        return self.get_product_row(product).find_element(
            By.CSS_SELECTOR,
            "td.cart_total"
        ).text.strip()

    def remove_product(self, product):

        row = self.get_product_row(product)

        delete_button = row.find_element(
            By.CSS_SELECTOR,
            "a.cart_quantity_delete"
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

        # Wait until the product row disappears
        self.wait.until(
            EC.staleness_of(row)
        )