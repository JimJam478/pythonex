import unittest
from pyex1 import panagram

class TestPanagram(unittest.TestCase):
    def testIsPanagram(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        self.assertTrue(panagram(sentence))

    def testIsNotPanagram(self):
        sentence = "the quick brown fox jumped over the lazy dog"
        self.assertFalse(panagram(sentence))
    
    def testNullInput(self):
        ret = panagram("")
        self.assertFalse(ret)


if __name__ == "__main__":
    unittest.main()
