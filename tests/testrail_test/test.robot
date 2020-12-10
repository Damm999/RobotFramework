*** Settings ***
Documentation     Test Rails Request
Library           RF
Suite Setup     test rails setup    ${url}    ${email}    ${password}

Variables       ../../confg/test_rails_variables.py

*** Variables ***


*** Test Cases ***
Get Request check
    [Documentation]    Sample check for test rails request operations
    [Tags]    sanitycheck

    Get All Tests    7
    Get Test    582

*** Keywords ***
