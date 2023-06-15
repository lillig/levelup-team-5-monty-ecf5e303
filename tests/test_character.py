from unittest import TestCase
from levelup.character import Character
from levelup.position_double import PositionDouble
from levelup.map_double import MapDouble

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        ARBITRARY_STEPS = 0
        DEFAULT_POSITION = PositionDouble((5,5))
        ARBITRARY_MAP = MapDouble(10,10)
        testobj = Character(ARBITRARY_NAME,ARBITRARY_STEPS,DEFAULT_POSITION, ARBITRARY_MAP)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
        self.assertEqual(ARBITRARY_STEPS, testobj.steps)
        self.assertEqual(DEFAULT_POSITION.coordinates,testobj.position.coordinates)
        self.assertEqual(ARBITRARY_MAP, testobj.map)

    def test_new_position(self):
        ARBITRARY_NAME = "MyName"
        ARBITRARY_STEPS = 0
        DEFAULT_POSITION = PositionDouble((5,5))
        ARBITRARY_MAP = MapDouble(10,10)
        testobj = Character(ARBITRARY_NAME,ARBITRARY_STEPS,DEFAULT_POSITION, ARBITRARY_MAP)
        new_position = testobj.calculatePosition('N', testobj.position.coordinates)
        self.assertEqual(new_position,(5,4))