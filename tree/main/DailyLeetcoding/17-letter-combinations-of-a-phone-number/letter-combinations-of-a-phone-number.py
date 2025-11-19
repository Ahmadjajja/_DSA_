class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapNumber = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }


        res = []

        def dfs(index, s):

            if index >= len(digits):
                res.append(s)
                return
            
            for ch in mapNumber[digits[index]]:
                
                dfs(index + 1, s + ch)

        dfs(0, "")

        return res
        