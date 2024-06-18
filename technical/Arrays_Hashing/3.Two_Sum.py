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
        return []