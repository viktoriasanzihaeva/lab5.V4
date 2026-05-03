import unittest
from vowels_count import count_vowels

class TestCountVowels(unittest.TestCase):

    def test_only_vowels_lowercase(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("aaa"), 3)

    def test_only_vowels_uppercase(self):
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("AAA"), 3)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("AbEcIdOfU"), 5)
        self.assertEqual(count_vowels("HeLLo"), 2)  # e, o

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels("123!@#"), 0)
        self.assertEqual(count_vowels(" "), 0)

    def test_with_spaces_and_punctuation(self):
        self.assertEqual(count_vowels("hello world"), 3)  # e, o, o
        self.assertEqual(count_vowels("a e i o u"), 5)
        self.assertEqual(count_vowels("Python is awesome!"), 6)  # o, i, a, e, o, e

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_single_character_vowel(self):
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("E"), 1)

    def test_single_character_consonant(self):
        self.assertEqual(count_vowels("b"), 0)
        self.assertEqual(count_vowels("Z"), 0)

    def test_digits_only(self):
        self.assertEqual(count_vowels("12345"), 0)

    def test_only_consonants(self):
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)
        self.assertEqual(count_vowels("BCDFG"), 0)

    def test_long_string(self):
        long_str = "a" * 1000 + "e" * 500
        self.assertEqual(count_vowels(long_str), 1500)

if __name__ == "__main__":
    unittest.main()
