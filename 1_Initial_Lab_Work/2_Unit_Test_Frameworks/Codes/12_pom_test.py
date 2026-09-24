from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()


class HomePage(BasePage):

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")

    def enter_name(self, name):
        self.driver.find_element(*self.NAME).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def name_is_visible(self):
        return self.driver.find_element(*self.NAME).is_displayed()


if __name__ == "__main__":

    driver = webdriver.Chrome()

    page = HomePage(driver)

    page.open("https://testautomationpractice.blogspot.com/")
    page.maximize()

    page.enter_name("Debanjali")
    page.enter_email("debanjali@gmail.com")

    assert page.name_is_visible()

    print("POM test executed successfully")

    page.close()