Feature: API Automation

  @smoke
  Scenario: Get a post
    Given the API is available
    When I send a GET request for post 1
    Then the response status code should be 200

  @regression
  Scenario Outline: Create posts using test data
    Given the API is available
    When I create a post with title "<title>", body "<body>" and user id <userId>
    Then the response status code should be 201

    Examples:
      | title            | body                 | userId |
      | Python API Test  | BDD API Automation   | 1      |
      | Second API Test  | Data Driven Testing  | 2      |