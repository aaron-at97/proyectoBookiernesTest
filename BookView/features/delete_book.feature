Feature: Delete book
  To keep my previous book records up to date
  as a editor
  I want to delete a record of books that I created, when we do not want that book to be available

  Background: Create Books state 0 for delete books
    Given I login as user "editor" with password "phantom123" with role "Writer"
    And To be treat book


  Scenario: Delete Book
    Then There are 3 books in library
    When Delete book
    Then There are 2 books in library

  Scenario: Acept and Delete Book
    Then There are 3 books in library
    When I acept Book
    And Delete book
    Then There are 2 books in library
    And There are 0 books acepted in library

  Scenario: Reject and Delete Book
    Then There are 3 books in library
    When I reject Book name Book "Ulises" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    And Delete book
    Then There are 2 books in library
    And There are 0 books reject in library
