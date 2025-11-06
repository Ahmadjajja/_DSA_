class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # there are 2 points:
        # 1. finding target is same as general bs
        start, end = -1, -1
        l, r = 0, len(nums) - 1
        targetIndex = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                targetIndex = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        # print(nums[targetIndex] if targetIndex > -1 else -1)
        if targetIndex == -1:
            return [-1, -1]

        # 2. find starting pos

        left, right = 0, targetIndex

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                start = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        # print("left, right -> ", left, right)

        # 2. find ending pos
        left, right = targetIndex, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                end = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        # print("left, right -> ", left, right)

        return [start, end]
        