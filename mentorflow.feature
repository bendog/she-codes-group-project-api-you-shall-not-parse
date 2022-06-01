
Feature: Mentor selfserve

    as a shecodes mentor I want to sign up to mentors events

    Scenario: register
    Given a user doesn't have an account
    When a user registers
    Then create an account
    And log the user in
    And return user preferences page

    Scenario: mentor preferences
    Given the mentor is auth.
    When when the user selecte their skillset from available roles from database
    Then record user selection as record in user.capabilities

    Scenario: available events list
    Given the mentor is auth.
    And the mentor has capabilities
    When the mentor selects available events
    Then show a list of EventModuleRoles which match user capabilities
    And allow user to select EventModuleRoles
    And record user selection in EventModuleRoles