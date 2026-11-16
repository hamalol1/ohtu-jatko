*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  123
    Set Password Confirmation  123
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Password Containing Only Letters
    Set Username  maija
    Set Password  abcdefgh
    Set Password Confirmation  abcdefgh
    Submit Credentials
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Password Confirmation That Does Not Match
    Set Username  maija
    Set Password  salasana123
    Set Password Confirmation  salasana321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Username already exists

*** Keywords ***
Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Welcome Page Should Be Open
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Get Title  ==  Register
    Get Text  body  *=  ${message}
