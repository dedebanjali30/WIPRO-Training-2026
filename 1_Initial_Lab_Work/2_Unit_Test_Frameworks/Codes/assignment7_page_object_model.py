from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*self.NAME).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def is_name_field_visible(self):
        return self.driver.find_element(
            *self.NAME
        ).is_displayed()


class LoginTest:

    def run_test(self):

        driver = webdriver.Chrome()

        try:
            driver.maximize_window()

            driver.get(
                "https://testautomationpractice.blogspot.com/"
            )

            page = LoginPage(driver)

            page.enter_name("Debanjali")
            page.enter_email("debanjali@gmail.com")

            # Assertion is outside the page locator definitions
            assert page.is_name_field_visible()

            print("ASSIGNMENT 7 - POM PASSED")

        finally:
            driver.quit()


if __name__ == "__main__":
    test = LoginTest()
    test.run_test()