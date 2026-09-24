*** Settings ***
Library    SeleniumLibrary
Resource   ../Resources/common_keywords.robot
Resource   ../TestData/login_data.robot

Test Teardown    Close All Browsers


*** Test Cases ***
Login With Multiple Users
    FOR    ${username}    IN    @{USERS}
        Open Browser    https://www.saucedemo.com/    chrome
        Maximize Browser Window

        Input Text    id=user-name    ${username}
        Input Text    id=password      ${PASSWORD}
        Click Button  id=login-button

        Log    Tested username: ${username}

        Close All Browsers
    END