Feature: Acept Book
  To keep my previous record books up to date As a publisher I want to accept book

  Background: Create Books state 0 for acept books
    Given I login as user "editor" with password "phantom123" with role "Writer"
    And To be treat book


  Scenario: Acept Book with treat
    When I acept Book
    Then There are 1 books acepted in library
    And There are 3 books in library


  Scenario: Acept two Books with treat
    When I acept Book
    And I acept Book
    Then There are 2 books acepted in library
    And There are 3 books in library

  Scenario: Acept in section rejected Books with treat
    When I reject Book name Book "Ulises" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    And I acept Book in section book rejected
    Then There are 0 books reject in library
    And There are 1 books acepted in library
    And There are 3 books in library