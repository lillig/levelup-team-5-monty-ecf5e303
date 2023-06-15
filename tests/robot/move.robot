*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     5              5            1                       NORTH         5           4           2
More in the middle of the board2    3              1            5                       WEST          2           2           6
Move in the SW Corner               0              9            7                       EAST          1           9           8
Move in the SE Corner               9              9           12                       EAST          9           9           13
Move in the NE Corner               9              0           34                       SOUTCH        9           1           35
Move in the NW Corner               0              0           55                       WEST          0           0           56


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