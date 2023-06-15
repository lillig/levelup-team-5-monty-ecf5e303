from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        ARBITRARY_STEPS = 0
        testobj = Character(ARBITRARY_NAME,ARBITRARY_STEPS)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
        self.assertEqual(ARBITRARY_STEPS, testobj.steps)