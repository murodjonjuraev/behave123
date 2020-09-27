Feature: Automation Practice Logo

  Scenario: Logo presence on Automation Practice home page
    Given User launch chrome browser
    When open Automation Practice homepage
    Then verify that the logo present on page
    And close browser
