class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # this is gonna store product of subarray
        product = 1
        countSubArr = 0

        # left, right -> gonna track every subarray one by one
        left = 0

        for r in range(len(nums)):
            product *= nums[r]

            while left < r and product >= k:
                product /= nums[left]
                left += 1

            if product < k:
                countSubArr += (r - left + 1)
        
        return countSubArr
            

            

            

                
        