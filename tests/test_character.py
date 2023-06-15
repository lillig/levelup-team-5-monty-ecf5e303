from unittest import TestCase
from levelup.character import Character
from levelup.position_double import PositionDouble

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        ARBITRARY_STEPS = 0
        DEFAULT_POSITION = PositionDouble((5,5))
        testobj = Character(ARBITRARY_NAME,ARBITRARY_STEPS,DEFAULT_POSITION)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
        self.assertEqual(ARBITRARY_STEPS, testobj.steps)
        self.assertEqual(DEFAULT_POSITION.coordinates,testobj.position.coordinates)