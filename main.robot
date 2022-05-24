*** Settings ***
Library    RequestsLibrary
Library    Utility.py

*** Test Cases ***
Test Case 1
    Create Session                             my_session            https://jsonplaceholder.typicode.com
    ${get_resp} =                              GET On Session        my_session                              /posts
    Dict List Should Contain Value             ${get_resp.json()}    id                                      1
    Dict List Should Not Contain Duplicates    ${get_resp.json()}    id
