*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://testautomationpractice.blogspot.com/
${BROWSER}   Chrome

*** Keywords ***
Open Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Enter User Details
    Input Text    id=name    Debanjali
    Input Text    id=email    debanjali@gmail.com

Close Website
    Close All Browsers