class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preFixSumCount = {0: 1}
        res = 0
        preFixSum = 0
        for num in nums:
            preFixSum += num

            if preFixSum - k in preFixSumCount:
                res += preFixSumCount[preFixSum - k]
            
            preFixSumCount[preFixSum] = 1 + preFixSumCount.get(preFixSum, 0)
        
        return res


        