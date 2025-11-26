class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0

        longest1s = 0
        countZeros = 0

        while r < len(nums):
            if countZeros > k:
                if nums[l] == 0:
                    countZeros -= 1
                l += 1
                continue

            longest1s = max(longest1s, r - l)
            if nums[r] == 0:
                countZeros += 1
            r += 1
        
        if countZeros <= k:
            longest1s = max(longest1s, r - l)

        return longest1s 


# tc = O(n)
# sc = O(1)


        