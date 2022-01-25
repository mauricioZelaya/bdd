Feature: test de funciones

  Scenario Outline: multiple rest
    Given we have two numbers "<a>" and "<b>"
    When we do an "<operation>"
    Then we will get the correct "<result>"

    Examples:
    |  a |  b | result | operation |
    |  2 |  2 |   0    |    rest   |
    | -2 |  2 |  -4    |    rest   |
    | -2 | -2 |   0    |    rest   |
    |  2 |  2 |   4    |    add   |
    | -2 |  2 |   0    |    add   |
    | -2 | -2 |   -4   |    add   |
    |  2 |  2 |   4    |    star   |
    | -2 |  2 |  -4    |    star   |
    | -2 | -2 |   4   |    star   |


