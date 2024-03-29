import unittest
from pyex1 import panagram
from pyex1 import palindrome
from pyex1 import freq

class TestPanagram(unittest.TestCase):
    def testIsPanagram(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        self.assertTrue(panagram(sentence))

    def testIsNotPanagram(self):
        sentence = "the quick brown fox jumped over the lazy dog"
        self.assertFalse(panagram(sentence))

    def testLangInput(self):
        lang = "ഓണം"
        self.assertFalse(panagram(lang))
    
    def testNullInput(self):
        ret = panagram("")
        self.assertFalse(ret)

class TestPalindrome(unittest.TestCase):
    def testIsPalindrome(self):
        string = "malayalam"
        self.assertTrue(palindrome(string))

    def testIsNotPalindrome(self):
        string = "coding"
        self.assertFalse(palindrome(string))
    
    def testNullInput(self):
        ret = palindrome("")
        self.assertTrue(ret)
    
    def testSingleInputPalindrome(self):
        ret = palindrome("z")
        self.assertTrue(ret)

class TestFreq(unittest.TestCase):
    def testFreq(self):
        String = "aabbbc"
        expected_dict = {'a':2,'b':3,'c':1}
        self.assertDictEqual(expected_dict,freq(String))
   
    def testSymbolsInput(self):
        symbols = "##"
        expected_dict = {'#':2}
        self.assertDictEqual(expected_dict,freq(symbols))
        

if __name__ == "__main__":
    unittest.main()
