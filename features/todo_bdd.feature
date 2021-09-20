Feature: to do tests

  Scenario: Add new task and see it in the list
    Given I am in the todos page
    When I add new task "Clean my house"
    Then the task "Clean my house" will be added to the list