class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                k -= 1
                stack.pop()
            stack.append(ch)
        if k > 0:
            stack = stack[:len(stack) - k]
        res = "".join(stack).lstrip("0")
        return  res if res != "" else "0"