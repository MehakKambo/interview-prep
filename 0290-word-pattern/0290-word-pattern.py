class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Create a dictionary to map pattern letters to words
        mappings = {}
        
        # Create a dictionary to map words to pattern letters (reverse mapping)
        reverse_mappings = {}
        
        # Split the input string `s` into a list of words
        s_parsed = s.split(" ")
        
        # If the number of pattern letters and words doesn't match, return False
        if len(pattern) != len(s_parsed):
            return False

        # Loop through each letter in the pattern and the corresponding word in s_parsed
        for i in range(len(pattern)):
            letter = pattern[i]    # Current letter in the pattern
            word = s_parsed[i]     # Corresponding word in the string `s`

            # Check if the letter is already mapped and if the mapped word doesn't match the current word
            if letter in mappings and mappings[letter] != word:
                return False
            
            # Check if the word is already mapped to a different letter in reverse_mappings
            if word in reverse_mappings and reverse_mappings[word] != letter:
                return False

            # Create or update the mapping from letter to word
            mappings[letter] = word
            
            # Create or update the reverse mapping from word to letter
            reverse_mappings[word] = letter

        # If all checks pass, return True (pattern matches the word sequence)
        return True
            
# Space: O(max(n, m)) = O(m) 
# n is the number of unique letters in pattern
# m is the size of the pattern
# 