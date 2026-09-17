class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Technique: XOR-based pairing/cancellation.
        # Every number that exists in both the expected range [0,n] and the array
        # appears exactly twice and cancels out (x ^ x = 0); the missing number
        # appears only once and survives as the final result.
        
        n = len(nums)
        result = n  # start with n, since range is [0, n] but index only covers [0, n-1]

        for i in range(n):
            result ^= i ^ nums[i]

        return result