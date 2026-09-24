*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close All Browsers


*** Test Cases ***
Open Website Smoke Test
    [Tags]    smoke
    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window
    Page Should Contain    Swag Labs


Login Regression Test
    [Tags]    regression
    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window
    Input Text    id=user-name    standard_user
    Input Text    id=password      secret_sauce
    Click Button  id=login-button
    Page Should Contain    Products