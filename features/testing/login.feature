# Created by  at 12/09/24
Feature: Login Page Functionality
  # Enter feature description here
@regression @valid_username
  Scenario Outline: Login with valid user credentials
    Given Open application and enter <username> with <password>
    When user clicks on login button
    Then Verify the user is successfully login
    Examples:
      | username | password |
      | testuser | Tanga321#|

  @regression
  Scenario: Login with Invalid user credentials
     Given Open application and enter invalid username with password
     When user clicks on login button
     Then Verify the use is not able to login