class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longestWindow = 0
        freqOnes = 0

        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                freqOnes += 1
            while freqOnes > k:
                if nums[l] == 0:
                    freqOnes -= 1
                l += 1
                
            windowSize = r - l + 1
            longestWindow = max(longestWindow, windowSize)
            
        
        return longestWindow

        # tc -> O(n)
        # sc -> O(1)









        