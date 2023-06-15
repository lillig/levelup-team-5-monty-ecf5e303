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