Feature: Create book
  Create new book in the library to accept or reject and have it reviewed by the editor
  as a writer
  I want to register a book with about a library

  Background: There is a registered user
    Given I login as user "testw" with password "phantom123" with role "Writer"
    When I register Book
      | id_book    | title         | genere  | body   |
      | Z65865432M | la celestina | Novela  | prueba2 |

  Scenario: Register just Book form
    When I register Book
      | id_book    | title         | genere  | body   |
      | T98765432M | canas y barro | Novela  | prueba |
    Then There are 2 books in library

  Scenario: Register the first book 1 user and another user 1 register books in the library
    Given I login as user "testw2" with password "phantom" with role "Writer"
    When I register Book
      | id_book    | title         | genere  | body   |
      | 358265436J | libro5 | Novela  | casa |
    Then There are 2 books in library

"""  Scenario: Register just restaurant name and city
    Given I login as user "user" with password "password"
    When I register restaurant
      | name        | city      | country   |
      | The Tavern  | London    | England   |
    Then I'm viewing the details page for restaurant by "user"
      | name        | city      | country   |
      | The Tavern  | London    | England   |
    And There are 1 restaurants

  Scenario: Try to register restaurant but not logged in
    Given I'm not logged in
    When I register restaurant
      | name        |
      | The Tavern  |
    Then I'm redirected to the login form
    And There are 0 restaurants"""
