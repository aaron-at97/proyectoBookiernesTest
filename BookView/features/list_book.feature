Feature: List Book HomePage
  To keep me updated about the online library registered in my library
  I want to list the first 4 books in the library on the home page, not register

  Background: There are 6 registered books library home page
    Given I Create Book

  Scenario: List the first 4 books
    When I list books
    Then I'm viewing a list containing
      | title     |
      | Ulises    |
      | Cañas y barro |
      | la celestina |
      | Principe del mal |
    And The list contains 4 books