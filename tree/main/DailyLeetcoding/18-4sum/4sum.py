class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         res = []

#         for i in range(n - 3):
#             # Skip duplicates for i
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             for j in range(i + 1, n - 2):
#                 # Skip duplicates for j
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue

#                 l, r = j + 1, n - 1

#                 while l < r:
#                     total = nums[i] + nums[j] + nums[l] + nums[r]

#                     if total < target:
#                         l += 1
#                     elif total > target:
#                         r -= 1
#                     else:
#                         res.append([nums[i], nums[j], nums[l], nums[r]])
#                         l += 1
#                         r -= 1

#                         # Skip duplicates for l and r
#                         while l < r and nums[l] == nums[l - 1]:
#                             l += 1
#                         while l < r and nums[r] == nums[r + 1]:
#                             r -= 1

#         return res
