Feature: Pickaboo Login Page

  Scenario:  Login with valid user id and password
    Given Lauch the Chrome
    When Open the Pickaboo Login Page
    And Enter Mobile Number "01726732321" and Password "rafat123"
    And Click on the login Button
    Then User Must successfull login


  Scenario Outline: Login Process With Multipul UsserId and password
    Given Lauch the Chrome
    When Open the Pickaboo Login Page
    And Enter Mobile Number "<Mobile Number>" and Password "<password>"
    And Click on the login Button
    Then User Must successfull login
    Examples:
      | Mobile Number | password  |
      | 01726732321   | rafat123  |
      | 01726732321   | rafat12   |