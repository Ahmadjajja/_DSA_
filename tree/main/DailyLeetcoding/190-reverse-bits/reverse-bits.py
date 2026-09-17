class Solution:
    def reverseBits(self, n: int) -> int:
        # Technique: bit-by-bit reconstruction via shift-and-OR.
        # For each of the 32 bits, extract n's rightmost bit (n & 1), then
        # push it into result's rightmost slot after shifting result left
        # to make room — building the reversed number one bit at a time.
        res = 0
        for _ in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1
        return res
        