Feature: Conversions

    Scenario Outline: Props
        Given a <moneyline>
        When we calculate the prop
        Then the prop of <prop> is correct

        Examples: Prop
        | moneyline     | prop               |
        | -100          | 0.5                |
        | -200          | 0.6666666666666666 | 
        | 100           | 0.5                |
        | 200           | 0.3333333333333333 |
        | -1900         | 0.95               |
        | 1900          | 0.05               |

    Scenario Outline: Payout
        Given a <moneyline>
        When we calculate the payout 
        Then the payout of <payout> is correct

        Examples: Payout
        | moneyline     | payout             | 
        | -100          | 2                  |
        | -200          | 1.5                |
        | 100           | 2                  | 
        | 200           | 3                  | 
        | -1900         | 1.0526315789473684 | 
        | 1900          | 20                 |
        