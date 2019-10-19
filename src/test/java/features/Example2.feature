Feature: String reverse?
  Method should reverse input string

  Scenario: Reverse input string
    Given Input string "qwertyuiop"
    When String is reversed
    Then Then output string is "poiuytrewq"

  Scenario: Reverse input string with spaces
    Given Input string "qw ertyu iop"
    When String is reversed
    Then Then output string is "poi uytre wq"