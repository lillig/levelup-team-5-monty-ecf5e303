from unittest import TestCase
from levelup.character import Character
from levelup.position_double import PositionDouble
from levelup.map_double import MapDouble

class TestCharacterInitWithName(TestCase):
    def setUp(self):
        self.ARBITRARY_NAME = "MyName"
        self.ARBITRARY_STEPS = 0
        self.DEFAULT_POSITION = PositionDouble((5,5))
        self.ARBITRARY_MAP = MapDouble(10,10)
        self.testobj = Character(self.ARBITRARY_NAME,self.ARBITRARY_STEPS,self.DEFAULT_POSITION, self.ARBITRARY_MAP)

    def test_init(self):
        self.assertEqual(self.ARBITRARY_NAME, self.testobj.name)
        self.assertEqual(self.ARBITRARY_STEPS, self.testobj.steps)
        self.assertEqual(self.DEFAULT_POSITION.coordinates,self.testobj.position.coordinates)
        self.assertEqual(self.ARBITRARY_MAP, self.testobj.map)

    def test_new_position(self):
        new_position = self.testobj.calculatePosition('N', self.testobj.position.coordinates)
        self.assertEqual(new_position,(5,4))

    def test_move(self):
        self.testobj.move('N')
        self.assertEqual(self.testobj.position.coordinates, (5,4))