Feature: DemoQA API Automation

  Scenario: Create user and rent books
    Given I create a new user in the system
    And I generate an access token
    Then the user should be authorized
    When I list all available books
    And I rent two chosen books
    Then I should see the rented books in the user details