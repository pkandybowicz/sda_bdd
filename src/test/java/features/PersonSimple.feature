Feature: Person simple class?
  Class should contain methods to manage persons

  Scenario: Person name is displayed correctly
    Given New person with first name "Karen" and last name "Smith" is created
    Then Then this person name is displayed as "Smith, Karen"