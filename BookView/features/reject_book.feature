Feature: Reject Book
  To keep my previous logbooks up to date As a publisher I want to reject the book

  Background: Create Books state 0 for reject books
    Given I login as user "editor" with password "phantom123" with role "Writer"
    And To be treat book


  Scenario: Reject Book with treat
    When I reject Book name Book "Ulises" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    Then There are 1 books reject in library
    And There are 3 books in library


  Scenario: Reject two Book with treat
    When I reject Book name Book "Ulises" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    And I reject Book name Book "Cañas y barro" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    Then There are 2 books reject in library
    And There are 3 books in library

  Scenario: Acept and Reject two Book with treat
    When I reject Book name Book "Ulises" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    And I acept Book
    Then There are 1 books reject in library
    And There are 1 books acepted in library
    And There are 3 books in library

  Scenario: Acept and Reject section acepted Books with treat
    When I acept Book
    And I reject Book name Book "Ulises" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    Then There are 1 books reject in library
    And There are 0 books acepted in library
    And There are 3 books in library