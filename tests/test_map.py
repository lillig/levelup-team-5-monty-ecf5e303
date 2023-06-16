from unittest import TestCase
from levelup.map import Map

class TestMap (TestCase):
    def setUp(self):
        self.HEIGHT = 10
        self.WIDTH = 10
        self.testobj = Map(self.HEIGHT,self.WIDTH)

    def test_init(self):
        self.assertEqual(self.HEIGHT, self.testobj.height)
        self.assertEqual(self.WIDTH, self.testobj.width)
    
    def test_validate_position(self):
        inputs = [[(8,5), (8,5)], [(2,-1), (2,0)], [(5,10), (5,9)], [(-1,7), (0,7)], [(10,2), (9,2)]]
        for i in inputs:
            validCoordinates = self.testobj.validatePosition(i[0])
            self.assertEqual(validCoordinates, i[1])