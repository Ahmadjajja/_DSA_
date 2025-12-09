class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # skipping duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num1 = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                num2 = nums[l]
                num3 = nums[r]
                s = num1 + num2 + num3
                if s == 0:
                    res.append([num1, num2, num3])
                    l += 1
                    r -= 1

                    # skipping duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s > 0:
                    r -= 1
                else:
                    l += 1
                
        
        return res

