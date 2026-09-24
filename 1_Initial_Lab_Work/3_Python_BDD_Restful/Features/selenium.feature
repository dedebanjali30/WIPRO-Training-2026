Feature: Selenium Browser Automation

  Scenario: Open website and enter user details
    Given I open the automation practice website
    When I enter my name
    And I enter my email
    Then the page should contain the name field