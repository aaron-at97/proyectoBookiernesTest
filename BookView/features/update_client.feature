Feature: Update Client
  Update data of client
  As a client
  I want to update a data with a about a user client

  Background: There is a registered user and restaurant
    Given I login as user "client" with password "masternum1" with role "Client"

  Scenario: modify namePage with client
    When I modify a namePage at client "Aaron Arenas Tomas"

  Scenario: modify telefon with client
    When I modify a telefon at client "698526312"

  Scenario: modify postal code with client
    When I modify a postal code at client "24123"

  Scenario: modify name with client
    When I modify a name at client "Aaron"

  Scenario: modify more than one element
    When I modify a name, telefon and email at client "Pau" "6852369912" "prueba@gmail.com"

  Scenario: modify all perfil user Client
    When I modify all elements
      | name               | nombre | apellido      | telefon   | correo            | codi_postal |
      | Aaron Arenas Tomas | Aaron  | Arenas Tomas  | 623456789 | prueba2@gmail.com | 25836       |