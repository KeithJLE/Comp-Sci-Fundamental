# CPE 101-01
# LAB 6: String Function Tests
# Name: Keith Lee
# Section: 7
# Date: 2/7/2022

import unittest
from str_funcs import *


class MyTestCase(unittest.TestCase):
    def test_vowel_extractor(self):
        self.assertEqual(vowel_extractor("This is a test."), "iiae")
        self.assertEqual(vowel_extractor("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), "AEIOUaeiou")
        self.assertEqual(vowel_extractor("The quick brown fox jumps over the lazy dog."), "euioouoeeao")

    def test_str_capitalize(self):
        self.assertEqual(str_capitalize("The quick brown fox jumps over the lazy dog."), "The Quick Brown Fox Jumps Over The Lazy Dog.")
        self.assertEqual(str_capitalize(" 123123    qqq ASD    ,.,.02a     pin@eapple  "), " 123123    Qqq ASD    ,.,.02a     Pin@eapple  ")
        self.assertEqual(str_capitalize("@3ASDF iiii80[] ,. poFSi     ()()w"), "@3ASDF Iiii80[] ,. PoFSi     ()()w")

    def test_str_rotate(self):
        self.assertEqual(str_rotate("The quick brown fox jumps over the lazy dog"), "Gur dhvpx oebja sbk whzcf bire gur ynml qbt")
        self.assertEqual(str_rotate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
        self.assertEqual(str_rotate("Keith Lee"), "Xrvgu Yrr")

    def test_make_substring(self):
        self.assertEqual(make_substring("The quick brown fox jumps over the lazy dog", 0, 20, 2), "Teqikbonfx")
        self.assertEqual(make_substring("Keith Lee Lab6", 4, 7, 1), "h L")
        self.assertEqual(make_substring("abbcccddddeeeeeffffff", 3, 19, 2), "ccddeeff")

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("anna"), True)
        self.assertEqual(is_palindrome("Annnnnnnnnna"), False)
        self.assertEqual(is_palindrome("1AnnA1"), True)

    def test_count_characters(self):
        self.assertEqual(count_characters("This is a test", "t"), 2)
        self.assertEqual(count_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123123", "a"), 1)
        self.assertEqual(count_characters("qqqQQQcounting    123 22  asdf jack[[ MM", "a"), 2)

if __name__ == '__main__':
    unittest.main()
