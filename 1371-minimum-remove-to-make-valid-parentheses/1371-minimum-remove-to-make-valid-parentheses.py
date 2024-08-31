class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        split = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                # if curr char is "(" then we push it to stack
                stack.append(i)
            
            elif s[i] == ')':
                # pop top of the stack
                if len(stack) != 0:
                    stack.pop()
                else:
                    #empty stack
                    split[i] = ""
        
        for i in stack:
            split[i] = ""
        
        return ''.join(split)