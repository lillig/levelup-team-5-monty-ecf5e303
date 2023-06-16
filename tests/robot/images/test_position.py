from unittest import TestCase
from levelup.position import Position
class TestPositionWithCoordinates(TestCase):
    def setUp(self):
        self.COORDINATES = (5,5)
        self.testobj = Position(self.COORDINATES)

    def test_init(self):
        self.assertEqual(self.COORDINATES, self.testobj.coordinates)
