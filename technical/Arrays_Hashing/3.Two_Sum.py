"""
PROBLEM STATEMENT:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

PROPOSED SOLUTION:
- Create a hashmap to store the index of each number
- Iterate through the array and check if the difference between 
    the target and the current number is in the hashmap
- If it is, return the indices of the two numbers
- Time Complexity: O(n) where n is the length of the array
- Space Complexity: O(n) because we store the indices of the numbers
- The time complexity is O(n) because we have to iterate through 
    the array to find the indices
"""

import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i
        return None
            
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_typical_case(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1], "Should return [0, 1] for numbers [2, 7] adding to 9")

    def test_no_solution(self):
        self.assertIsNone(self.solution.twoSum([1, 2, 3], 7), "Should return None if no two numbers sum to the target")

    def test_multiple_solutions(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2], "Should return the first correct pair [1, 2] for numbers [2, 4] adding to 6")

    def test_negative_numbers(self):
        self.assertEqual(self.solution.twoSum([-1, -2, -3, -4], -6), [1, 3], "Should return [1, 3] for numbers [-2, -4] adding to -6")

    def test_zero_and_positive_numbers(self):
        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [0, 3], "Should return [0, 3] for zeros adding to 0")

if __name__ == '__main__':
    unittest.main(verbosity=2)