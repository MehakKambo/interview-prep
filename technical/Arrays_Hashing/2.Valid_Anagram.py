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
        return