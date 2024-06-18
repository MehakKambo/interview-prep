"""
PROBLEM STATEMENT:
Given two strings s and t, return true if 
t is an anagram of s, and false otherwise.

PROPOSED SOLUTION:
- If lens dont match, return False
- Count the frequency of each character in s and t
- If the frequencies match, return True
- Time Complexity: O(n) where n is the length of the strings
- Space Complexity: O(1) because the hashmaps will have at 
    most 26 characters
- The time complexity is O(n) because we have to iterate 
    through the strings to count the frequencies
"""
import unittest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = {}
        freq_t = {}
        
        for i in range(len(s)):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        
        return freq_s == freq_t
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_anagram_positive(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"), "Should return True for anagrams")
        self.assertTrue(self.solution.isAnagram("listen", "silent"), "Should return True for anagrams")

    def test_anagram_negative(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"), "Should return False for non-anagrams")
        self.assertFalse(self.solution.isAnagram("hello", "world"), "Should return False for non-anagrams")

    def test_different_lengths(self):
        self.assertFalse(self.solution.isAnagram("abc", "ab"), "Should return False if strings are of different lengths")

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""), "Should return True for two empty strings")

    def test_case_sensitivity(self):
        self.assertFalse(self.solution.isAnagram("a", "A"), "Should return False if cases are different")

    def test_special_characters(self):
        self.assertTrue(self.solution.isAnagram("a b$c", "b$ca "), "Should return True for anagrams with special characters")

if __name__ == '__main__':
    unittest.main(verbosity=2)