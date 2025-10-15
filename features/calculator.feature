Feature: Calculator Functionality

  Scenario: Basic Arithmetic Operations
    Given I have opened the calculator
    When I input "2" and press "+" and input "3"
    Then the result should be "5"
    
  Scenario: Subtraction Operation
    Given I have opened the calculator
    When I input "5" and press "-" and input "2"
    Then the result should be "3"

  Scenario: Multiplication Operation
    Given I have opened the calculator
    When I input "4" and press "*" and input "3"
    Then the result should be "12"

  Scenario: Division Operation
    Given I have opened the calculator
    When I input "6" and press "/" and input "2"
    Then the result should be "3"

  Scenario: Clear Functionality
    Given I have opened the calculator
    When I input "5" and press "C"
    Then the display should be empty

  Scenario: Equals Functionality
    Given I have opened the calculator
    When I input "2" and press "+" and input "3" and press "="
    Then the result should be "5"

  Scenario: Cat Operator Functionality
    Given I have opened the calculator
    When I input "2" and press "🐱" and input "3"
    Then the result should be "13"

  Scenario: Cat Operator with Same Numbers
    Given I have opened the calculator
    When I input "2" and press "🐱" and input "2"
    Then the result should be "10"

  Scenario: Cat Operator with Different Numbers
    Given I have opened the calculator
    When I input "1" and press "🐱" and input "3"
    Then the result should be "11"