Feature: Automation Practice Login

  Scenario: Login to Automation Practice with valid parameters
    Given I launch Chrome browser
    When I open Automation Practice home page
    And I click on Sign in button
    And Enter email address "vasya@email.com" and password "abcd1234"
    And Click on login button
    Then User must successfully login to My account page
