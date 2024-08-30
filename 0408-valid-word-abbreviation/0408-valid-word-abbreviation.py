class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Initialize pointers for both the word and abbreviation
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # If the abbreviation starts with a '0', it's invalid
                if abbr[j] == '0':
                    return False
                
                # Calculate the number represented by the digits in the abbreviation
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                # Move the pointer in the original word forward by the number
                i += num
            else:
                # If the characters at the current pointers do not match, return False
                if word[i] != abbr[j]:
                    return False
                
                # Move both pointers forward if characters match
                i += 1
                j += 1

        # Check if both pointers have reached the end of their respective strings
        return i == len(word) and j == len(abbr)
                