"""
PROBLEM STATEMENT:
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct.

PROPSED SOLUTION:
 - Create a hash set to store the numbers that have been seen so far
 - Iterate through the list of numbers, if the number is in hashset, return True
    because that means it has been seen before and we have found our duplicate
 - If the number is not in the hashset, add it to the hashset and continue
 - If we finish iterating through the list without finding a duplicate, return False
 - Time complexity: O(n) where n is the number of elements in the list
 - Space complexity: O(n) where n is the number of elements in the list
 - The space complexity is O(n) because in the worst case, we will have to store 
    all the elements in the list in the hashset
 - The time complexity is O(n) because we have to iterate through the list once
    to check for duplicates
"""

import unittest
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
                
        return False
    

class TestHasDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_empty_list(self):
        self.assertFalse(self.solution.hasDuplicate([]), "Should return False for an empty list")

    def test_no_duplicates(self):
        self.assertFalse(self.solution.hasDuplicate([1, 2, 3, 4, 5]), "Should return False for a list with no duplicates")
        self.assertFalse(self.solution.hasDuplicate([10, -10, 100, -100]), "Should return False for a list with negative numbers and no duplicates")

    def test_with_duplicates(self):
        self.assertTrue(self.solution.hasDuplicate([1, 2, 2, 3, 4]), "Should return True for a list with duplicates")
        self.assertTrue(self.solution.hasDuplicate([0, 0]), "Should return True for a list with zero duplicates")

    def test_single_element(self):
        self.assertFalse(self.solution.hasDuplicate([1]), "Should return False for a single-element list")

    def test_negatives_and_zero(self):
        self.assertFalse(self.solution.hasDuplicate([-1, 0, 1, 2, 3]), "Should return False for a list with negatives and zero without duplicates")
        self.assertTrue(self.solution.hasDuplicate([0, -1, 1, 0]), "Should return True for a list with zero as a duplicate")

if __name__ == '__main__':
    unittest.main(verbosity=2)