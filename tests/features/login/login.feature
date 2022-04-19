Feature: Login

  Scenario: Acceptance test - Login
    Given the automation practice page is displayed
    When I click on 'Sing in' button
    And I log in as 'User1'
    Then My account page is displayed
    And User name: 'Test New' is displayed in navigation bar