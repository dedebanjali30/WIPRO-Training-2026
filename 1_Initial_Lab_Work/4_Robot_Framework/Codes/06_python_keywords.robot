*** Settings ***
Library    custom_keywords.py


*** Test Cases ***
Python Custom Keyword Test

    ${total}=    Calculate Total    500    3

    Log    Total price: ${total}

    ${result}=    Check Positive Number    ${total}

    Should Be True    ${result}

    Log    Python custom keyword executed successfully