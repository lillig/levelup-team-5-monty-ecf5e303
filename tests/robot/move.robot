*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Mid-N                               5              5            42                    NORTH         5           4           43
Mid-S                               5              5            57                    SOUTH         5           6           58
Mid-E                               5              5            75                    EAST          6           5           76
Mid-W                               5              5            17                    WEST          4           5           18
NW Corner N                         0              0            103                   NORTH         0           0           104
NW Corner S                         0              0            32                    SOUTH         0           1           33
NW Corner E                         0              0            1                     EAST          1           0           2
NW Corner W                         0              0            20                    WEST          0           0           21
SW Corner N                         0              9            57                    NORTH         0           8           58
SW Corner S                         0              9            38                    SOUTH         0           9           39
SW Corner E                         0              9            9                     EAST          1           9           10
SW Corner W                         0              9            25                    WEST          0           9           26
SE Corner N                         9              9            58                    NORTH         9           8           59
SE Corner S                         9              9            83                    SOUTH         9           9           84
SE Corner E                         9              9            9                     EAST          9           9           10
SE Corner W                         9              9            4                     WEST          8           9           5
NE Corner N                         9              0            768                   NORTH         9           0           769
NE Corner S                         9              0            22                    SOUTH         9           1           23
NE Corner E                         9              0            83                    EAST          9           0           84
NE Corner W                         9              0            36                    WEST          8           0           37

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}