from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product-information')]//h2")
    QUANTITY = (By.CSS_SELECTOR, "input#quantity")
    ADD_TO_CART = (By.CSS_SELECTOR, "button.cart")
    VIEW_CART = (By.XPATH, "//div[contains(@class,'modal-content')]//a[contains(@href,'/view_cart')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_product_page_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME)).is_displayed()

    def set_quantity(self, quantity):
        field = self.wait.until(EC.visibility_of_element_located(self.QUANTITY))
        field.clear()
        field.send_keys(str(quantity))

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()

    def click_view_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.VIEW_CART)).click()
