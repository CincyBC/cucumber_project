Feature: Get Order API

  Scenario: Get existing order
    Given an order exists in the database with ID 1
    When I request the order with ID 1
    Then the API should return the order details

  Scenario: Get non-existent order
    Given no order exists in the database with ID 999
    When I request the order with ID 999
    Then the API should return a 404 error
