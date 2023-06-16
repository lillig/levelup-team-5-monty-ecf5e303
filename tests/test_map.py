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

    def test_calculate_position(self):
        inputs = [['N',(4,3), (4,2)], ['S', (6,8), (6,9)], ['E', (3,6), (4,6)], ['W', (8,2), (7,2)], ['W', (0,3), (0,3)]]
        for i in inputs:
            newCoordinates = self.testobj.calculatePosition(i[0], i[1])
            self.assertEqual(newCoordinates, i[2])