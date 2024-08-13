class Solution:
    def isPalindrome(self, s: str) -> bool:

        parsed_string = ""

        for char in s:
            if char.isalnum():
                parsed_string += char
            
        left, right = 0, len(parsed_string) - 1
        parsed_string = parsed_string.lower()
        while left < right:
            if parsed_string[left] != parsed_string[right]:
                return False

            left += 1
            right -= 1
            
        return True