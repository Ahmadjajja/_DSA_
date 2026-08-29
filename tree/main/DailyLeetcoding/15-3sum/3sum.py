class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            a = nums[i]

            # 2 pointer approach

            left, right = i + 1, len(nums) - 1

            while left < right:
                b, c = nums[left], nums[right]
                tot = a + b + c

                if tot > 0:
                    right -= 1
                elif tot < 0:
                    left += 1
                else:
                    res.append([a, b, c])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res