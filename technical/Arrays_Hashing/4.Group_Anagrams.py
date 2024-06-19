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
        if len(strs) < 2:
            return [strs]
        anagrams = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
            
        return anagrams.values()
    
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_typical_case(self):
        self.assertEqual(sorted(self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])),
                         sorted([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
                         "Should correctly group anagrams")

    def test_no_anagrams(self):
        self.assertEqual(sorted(self.solution.groupAnagrams(["abc", "def", "ghi"])),
                         sorted([["abc"], ["def"], ["ghi"]]),
                         "Should handle list with no anagrams")

    def test_all_anagrams(self):
        self.assertEqual(sorted(self.solution.groupAnagrams(["a", "a", "a"])),
                         sorted([["a", "a", "a"]]),
                         "Should handle list where all elements are anagrams")

    def test_empty_list(self):
        self.assertEqual(self.solution.groupAnagrams([]),
                         [[]],
                         "Should return empty list for empty input")

    def test_single_word(self):
        self.assertEqual(self.solution.groupAnagrams(["abc"]),
                         [["abc"]],
                         "Should handle single word input")

if __name__ == '__main__':
    unittest.main(verbosity=3)