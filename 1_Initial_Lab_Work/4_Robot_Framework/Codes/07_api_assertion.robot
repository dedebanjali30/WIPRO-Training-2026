*** Settings ***
Library    RequestsLibrary


*** Test Cases ***
Verify API Response

    Create Session
    ...    jsonplaceholder
    ...    https://jsonplaceholder.typicode.com

    ${response}=    GET On Session
    ...    jsonplaceholder
    ...    /posts/1

    Should Be Equal As Integers
    ...    ${response.status_code}
    ...    200

    Log    API status code: ${response.status_code}

    Should Be Equal As Strings
    ...    ${response.json()}[id]
    ...    1

    Log    API assertion passed