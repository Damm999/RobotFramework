*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Suite Setup       Go to HomePage
Suite Teardown    Close All Browsers

*** Variables ***
${LOGIN URL}      https://www.amazon.in
${BROWSER}        Chrome

*** Test Cases ***
User Must Sign in to checkout
    [documentation]     Amazon serach action
    [tags]      Regression
    Amazon and Search   laptop  laptop

*** Keywords ***
Amazon and Search
    [Arguments]     ${searchKey}    ${res}
    Input Text      id=twotabsearchtextbox   ${searchKey}
    Click Element   id=nav-search-submit-text
    Wait Until Page Contains    ${res}
Go to HomePage
    Open Browser    ${LOGIN URL}    ${BROWSER}