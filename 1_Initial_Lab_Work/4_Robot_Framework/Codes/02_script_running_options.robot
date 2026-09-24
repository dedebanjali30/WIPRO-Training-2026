*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://testautomationpractice.blogspot.com/
${BROWSER}   Chrome

*** Test Cases ***
Run Browser Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Automation Testing Practice
    Log    Test executed successfully
    Close All Browsers