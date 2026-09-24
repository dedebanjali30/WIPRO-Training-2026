*** Settings ***
Resource    ../Resources/common_keywords.robot

Test Setup       Open Website
Test Teardown    Close Website

*** Test Cases ***
Verify Website
    Title Should Be    Automation Testing Practice

Enter User Details
    Enter User Details