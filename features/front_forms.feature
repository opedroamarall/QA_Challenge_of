Feature: DemoQA UI Automation

  Scenario: Scenario 01 - Practice Form Submission
    Given I navigate to the Practice Form page
    When I fill out the form and submit it
    Then the success modal should be displayed with "Thanks for submitting the form"

  Scenario: Scenario 02 - Browser Windows
    Given I navigate to the "browser-windows" page
    When I click the New Window button
    Then a new window should open with the text "This is a sample page"

  Scenario: Scenario 03.1 - Web Tables Basic CRUD
    Given I navigate to the "webtables" page
    When I create a new form, edit it and then delete it
    Then the table should reflect the changes correctly

  Scenario: Scenario 03.2 - Bulk forms with 12 users
    Given I navigate to the "webtables" page
    When I create 12 new forms in the table
    And I delete all forms from the table
    Then the table should be empty

  Scenario: Scenario 04 - Progress Bar
    Given I navigate to the "progress-bar" page
    When I start the progress bar and stop before 25%
    And I wait for it to reach 100% and reset it
    Then the progress bar should return to 0%

  Scenario: Scenario 05 - Sortable numbers list
    Given I navigate to the "sortable" page
    When I reorder the list to the opposite order
    Then the list order should be toggled successfully