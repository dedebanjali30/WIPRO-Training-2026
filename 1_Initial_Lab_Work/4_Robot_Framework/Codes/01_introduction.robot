*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://testautomationpractice.blogspot.com/
${BROWSER}   Chrome

*** Test Cases ***
Open Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Automation Testing Practice
    [Teardown]    Close All Browsers

Enter Text In Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    id=name    Debanjali
    Input Text    id=email    debanjali@gmail.com
    Log    Text entered successfully
    [Teardown]    Close All Browsers