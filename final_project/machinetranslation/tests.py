import unittest
from translator import english_to_french
from translator import french_to_english

class Test_translator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNone(None, '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        self.assertIsNone(None, '')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
unittest.main()
