from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL = (
        By.CSS_SELECTOR,
        "input[data-qa='login-email']"
    )

    PASSWORD = (
        By.CSS_SELECTOR,
        "input[data-qa='login-password']"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-qa='login-button']"
    )

    LOGGED_IN_USER = (
        By.XPATH,
        "//a[contains(text(),'Logged in as')]"
    )

    LOGIN_ERROR = (
        By.XPATH,
        "//p[contains(text(),'Your email or password is incorrect!')]"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def is_login_page_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        ).is_displayed()

    def login(self, email, password):

        email_field = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        )

        email_field.clear()
        email_field.send_keys(email)

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        )

        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(
            EC.presence_of_element_located(
                self.LOGIN_BUTTON
            )
        )

        # Scroll button into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            login_button
        )

        # JavaScript click prevents advertisement
        # iframe from intercepting the click
        self.driver.execute_script(
            "arguments[0].click();",
            login_button
        )

    def is_logged_in(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.LOGGED_IN_USER
            )
        ).is_displayed()

    def get_login_error(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.LOGIN_ERROR
            )
        )

        return error.text.strip()