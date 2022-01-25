Feature: test de funciones

  Scenario Outline: multiple rest
    Given we have two numbers "<a>" and "<b>"
    When we rest a-b
    Then we will get the correct "<result>"

    Examples:
    |  a |  b | result |
    |  2 |  2 |   0    |
    | -2 |  2 |  -4    |
    | -2 | -2 |   0    |


  Scenario Outline: multiple additions
    Given we have two numbers "<a>" and "<b>"
    When we add a+b
    Then we will get the correct "<result>"

    Examples:
    |  a |  b | result |
    |  2 |  2 |   4    |
    | -2 |  2 |   0    |
    | -2 | -2 |   -4   |