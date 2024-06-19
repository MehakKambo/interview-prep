"""
PROBLEM STATEMENT:
- Given an array of strings, group anagrams together.
- An Anagram is a word or phrase formed by rearranging the letters of 
    a different word or phrase, typically using all the original letters exactly once.

PROPOSED SOLUTION:
- Create a hashmap to store the 


"""

import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return [[]]