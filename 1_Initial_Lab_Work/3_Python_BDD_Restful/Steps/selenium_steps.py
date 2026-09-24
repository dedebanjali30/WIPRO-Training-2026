from behave import given, when, then
from selenium import webdriver
from Pages.home_page import HomePage


@given("I open the automation practice website")
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get(
        "https://testautomationpractice.blogspot.com/"
    )
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)


@when("I enter my name")
def step_enter_name(context):
    context.home_page.enter_name("Debanjali")


@when("I enter my email")
def step_enter_email(context):
    context.home_page.enter_email("debanjali@gmail.com")


@then("the page should contain the name field")
def step_verify_name(context):
    assert context.home_page.name_is_visible()
    context.driver.quit()