class Solution:
    def isValid(self, s: str) -> bool:


        hm = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for ch in s:            
            if ch in hm:
                if stack and hm[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return not stack
        