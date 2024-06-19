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
    