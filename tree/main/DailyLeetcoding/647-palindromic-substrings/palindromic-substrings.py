class Solution:
    def countSubstrings(self, st: str) -> int:

        count = 0
        for i in range(len(st)):
            count += 1

            # check for odd 
            l, r = i - 1, i + 1

            while 0 <= l < len(st) and 0 <= r < len(st) and st[l] == st[r]:
                count += 1
                l -= 1
                r += 1

            # check for even
            l, r = i, i + 1

            while 0 <= l < len(st) and 0 <= r < len(st) and st[l] == st[r]:
                count += 1
                l -= 1
                r += 1
        
        return count

# TC: O(n2)
# SC: O(1)
