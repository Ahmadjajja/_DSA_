class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = right
        while left <= right:
            eatingSpeed = (left + right) // 2
            
            countH = 0
            for pile in piles:
                countH += math.ceil(pile / eatingSpeed)

            if countH <= h:
                k = min(k, eatingSpeed)
            
            if countH > h:
                left = eatingSpeed + 1
            else:
                right = eatingSpeed - 1
        
        return k

            

            


        