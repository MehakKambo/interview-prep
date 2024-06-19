"""
PROBLEM STATEMENT:
Given a string s, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.

PROPOSED SOLUTION:
- We can use two pointers to solve this problem
- Create a new string that contains only alphanum chars
- Use two pointers to compare the chars of the new string from the beginning and the end
- if the chars dont match before the pointers cross each other, return False; otherwise return True
- Time Complexity: O(n) because we are iterating through the same string twice (one to create the 
    new string and one to compare the chars) so the time complexity is O(n + n) = O(n)
- Space Complexity: O(m) where m is the number of alphanum chars in the string
"""

import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()
        
        left, right = 0, len(new_string) - 1
        
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            
            left += 1
            right -= 1
        return True
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_typical_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man a plan a canal Panama"), "Should return True for a valid palindrome")

    def test_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("hello world"), "Should return False for non-palindromic strings")

    def test_case_insensitivity(self):
        self.assertTrue(self.solution.isPalindrome("RaceCar"), "Should return True, ignoring cases")

    def test_alphanumeric_filter(self):
        self.assertTrue(self.solution.isPalindrome("Madam, I'm Adam."), "Should return True, ignoring non-alphanumeric characters")

    def test_single_character(self):
        self.assertTrue(self.solution.isPalindrome("a"), "Should return True for a single character")

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(""), "Should return True for an empty string")

    def test_long_palindrome(self):
        long_palindrome = "A" * 1000
        self.assertTrue(self.solution.isPalindrome(long_palindrome), "Should return True for a long palindromic string")

    def test_long_non_palindrome(self):
        long_non_palindrome = "A" * 500 + "B" * 500
        self.assertFalse(self.solution.isPalindrome(long_non_palindrome), "Should return False for a long non-palindromic string")

if __name__ == '__main__':
    unittest.main(verbosity=2)