import unittest
from translator import english_to_french, french_to_english, ApiException

class TestTranslatorEN2FR(unittest.TestCase):
    def test_null(self):
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french(None), "")
            
    def test_simple_word(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        
class TestTranslatorFR2EN(unittest.TestCase):
    def test_null(self):
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english(None), "")
            
    def test_simple_word(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()