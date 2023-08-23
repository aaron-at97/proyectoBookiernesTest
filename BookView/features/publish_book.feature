Feature: Publish Book
  To keep my old book records posted
  as a editor
  I want to edit a book record that I created was previously accepted

  Background: Create Books state 0 for acept books
    Given I login as user "editor" with password "phantom123" with role "Writer"
    And To be treat book


  Scenario: Publicate Book
    When I acept Book
    And I publicate Book Web
    Then There are 0 books acepted in library
    And There are 1 books publicate in library

  Scenario: Publicate and not Books acepted
    When No acetepted for publicate Book Web
    Then There are 0 books acepted in library
    And There are 0 books publicate in library
    And There are 3 books in library

  Scenario: Acept two Reject and publish Books with treat
    When I acept Book
    And I acept Book
    And I reject Book name Book "Ulises" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    And I reject Book name Book "Cañas y barro" motive "- El tema de su libro está pasado de moda,- Poca originalidad - Uso de lenguaje y estilo incorrecto"
    And I acept Book
    And I publicate Book Web
    Then There are 0 books acepted in library
    And There are 2 books reject in library
    And There are 1 books publicate in library
    And There are 3 books in library
