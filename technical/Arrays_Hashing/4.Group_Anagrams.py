"""
PROBLEM STATEMENT:
- Given an array of strings, group anagrams together.
- An Anagram is a word or phrase formed by rearranging the letters of 
    a different word or phrase, typically using all the original letters exactly once.

PROPOSED SOLUTION:
- Create a hashmap where the key is an array that counts the number of each letter 
    in the word. The value is a list of words that have the same count of letters.
- Iterate through the list of words and add them to the hashmap.
- Return the values of the hashmap.
- Time Complexity: O(N * K), where N is the number of words and K is the length of 
    the longest word.
- Space Complexity: O(N * K), where N is the number of words and K is the length of
    the longest word.
"""

import collections, unittest
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
            
        return anagrams.values()
    
    
