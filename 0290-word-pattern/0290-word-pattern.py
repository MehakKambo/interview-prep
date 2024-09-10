class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mappings = {}
        s_parsed = s.split(" ")
        if len(pattern) != len(s_parsed):
            return False

        for i in range(len(pattern)):
            # if char in mappings and the current char has diff value
            # return false
            letter = pattern[i]
            word = s_parsed[i]
            if letter in mappings and (mappings[letter] != word):
                return False
            elif letter not in mappings and word in mappings.values():
                return False
            else:
                mappings[pattern[i]] = s_parsed[i]
        return True
            
