from unittest import TestCase
from levelup.character import Character

class CharacterDouble(TestCase):
    def setUp(self):
        self.ARBITRARY_NAME = "MyName"
        self.testobj = Character(self.ARBITRARY_NAME)

    def test_init(self):
        self.assertEqual(self.ARBITRARY_NAME, self.testobj.name)
