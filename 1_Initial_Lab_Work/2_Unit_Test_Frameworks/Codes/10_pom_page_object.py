from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*self.NAME).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def name_is_visible(self):
        return self.driver.find_element(*self.NAME).is_displayed()


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    page = HomePage(driver)

    page.enter_name("Debanjali")
    page.enter_email("debanjali@gmail.com")

    assert page.name_is_visible()

    print("Page Object executed successfully")

    driver.quit()