from unittest import TestCase
from levelup.controller import GameController
from levelup.character_double import CharacterDouble


class TestGameController(TestCase):
    def setUp(self):
        self.testObj = GameController()

    def test_init(self):
        assert self.testObj.status != None

    def start_game(self):
        self.map = Map()
        if self.character == None:
            self.create_character(DEFAULT_CHARACTER_NAME)
        self.character.enter_map(self.map)
        self.status.running = True
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = 0

    def test_create_character(self):
        name = 'Monty'
        testCharacter = CharacterDouble(name)
        self.testObj.create_character(name)
        self.assertEqual(self.testObj.character.name, testCharacter.name)