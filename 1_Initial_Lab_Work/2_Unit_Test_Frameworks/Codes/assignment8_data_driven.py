import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def read_test_data():

    with open(
        "TestData/assignment8_login_data.csv",
        "r"
    ) as file:

        return list(csv.DictReader(file))


def run_login_test(row):

    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    try:

        driver.get("https://www.saucedemo.com/")

        driver.find_element(
            By.ID, "user-name"
        ).send_keys(row["username"])

        driver.find_element(
            By.ID, "password"
        ).send_keys(row["password"])

        driver.find_element(
            By.ID, "login-button"
        ).click()

        expected = row["expected"] == "True"

        if expected:

            assert "inventory.html" in driver.current_url

        else:

            error = driver.find_element(
                By.CSS_SELECTOR,
                "[data-test='error']"
            )

            assert error.is_displayed()

        return True

    finally:

        driver.quit()


if __name__ == "__main__":

    data = read_test_data()

    passed = 0

    for row in data:

        print(
            f"Testing: {row['username']}"
        )

        if run_login_test(row):

            passed += 1

            print("PASS")

    print(
        f"\nASSIGNMENT 8 - DDT PASSED: "
        f"{passed}/{len(data)}"
    )