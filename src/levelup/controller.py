import logging
from levelup.character import Character
from dataclasses import dataclass
from enum import Enum


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:

    character = None
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        pass

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.character = Character(character_name, 0, (5,5))
        else:
            self.character = Character(DEFAULT_CHARACTER_NAME, 0, (5,5))

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        pass

    def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10

    
