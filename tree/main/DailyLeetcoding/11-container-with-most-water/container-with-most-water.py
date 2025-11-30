class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(height) - 1

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            maxWater = max(maxWater,h * w)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxWater

# tc: O(n)
# sc: O(1)

        