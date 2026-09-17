class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1   # check rightmost bit
            n >>= 1          # shift right, drop that bit
        return count