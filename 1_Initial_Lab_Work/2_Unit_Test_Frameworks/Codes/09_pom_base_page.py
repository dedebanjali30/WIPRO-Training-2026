from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()


if __name__ == "__main__":

    driver = webdriver.Chrome()

    page = BasePage(driver)

    page.open("https://testautomationpractice.blogspot.com/")
    page.maximize()

    print("Base Page opened successfully")

    page.close()