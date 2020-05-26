Feature: Duck Duck Go searching

    Scenario Outline: Results
        Given I load the website
        When I search for "<phrase>"
        Then The result contains "<phrase>"
        Examples:
            | phrase              |
            | Whatever            |
            | Whenever            |

