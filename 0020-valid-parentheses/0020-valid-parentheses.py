class Solution:
    def isValid(self, s: str) -> bool:
        
        # Map = {")": "(", "}": "{", "]": "["}
        # stack = []
        # for c in s:
        #     #If the current character is an opening bracket.
        #     if c in '[({':
        #         stack.append(c)
        #         continue
        #     # The mapping for the opening bracket in our hash and the top
        #     # element of the stack don't match, return False
        #     #if stack is not empty or the top of our stack does not match to 
        #     # the opening bracket, return False
        #     if not stack or stack[-1] != Map[c]:
        #         return False
        #     stack.pop()

        # return not stack #true for empty stack bcz not stack

        mappings = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char in "{([":
                stack.append(char)
                continue
            
            if not stack or stack[-1] != mappings[char]:
                return False
            stack.pop()
        return not stack