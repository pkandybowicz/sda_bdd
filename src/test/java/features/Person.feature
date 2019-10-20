Feature: Person management
  Methods should allow to set basic information about person

  Scenario: Name in correctly displayed
    When new person with name "Anna" and surname "Kowalska" is created
    Then Person name is displayed as "Kowalska, Anna"