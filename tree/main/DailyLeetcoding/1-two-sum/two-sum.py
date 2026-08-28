class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # what would be len of nums? 
        # [2, 7, 11, 15]
        # is it sorted already?

        # 1. brute force -> O(n2)
        # 2. little better solution -> O(nlogn)
        # 3. tc -> O(n), sc -> O(n)

        hm = {}
        {3: 0, 4: 1, }

        for i in range(len(nums)):
            n = nums[i]
            if n in hm: # constant lookup
                return [hm[n], i]
            
            secondElem = target - n
            hm[secondElem] = i

        # {
        #    7 : 0,
        #    
        # 
        #  }


        # -ve or +ve nums?
        # how big 1 number might be?
        # -ve or +ve target?
        # how big 1 target might be?



        