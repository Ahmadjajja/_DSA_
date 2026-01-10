class Solution:
    def search(self, nums: List[int], target: int) -> bool:

# 1. first of all we've check like on which sorted part of the arr we are
# 2. act accordingly
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            
            # if duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # right sorted part
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid  - 1
                else:
                    left = mid + 1
        
        return False
