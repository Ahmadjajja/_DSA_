class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search on the answer: search over possible ship capacities.
        # Pattern: "minimize the max/capacity such that some constraint is satisfiable"
        # lower bound = max single weight (ship must at least carry the heaviest item)
        # upper bound = sum of all weights (ship everything in one day)
        l, r = max(weights), sum(weights)
        res = r

        # Greedy feasibility check: can we ship everything within `days`
        # if the ship's capacity is `cap`?
        def canShip(cap):
            ships, currCap = 1, 0
            for w in weights:
                # current item doesn't fit on today's load, start a new day
                if currCap + w > cap:
                    ships += 1
                    if ships > days:
                        return False  # exceeded allowed days, cap too small
                    currCap = 0

                currCap += w
            return True

        # Search space is monotonic: if `cap` works, every larger cap also works.
        # So we binary search for the smallest cap that still works.
        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)  # cap works, try to shrink it further
                r = cap - 1
            else:
                l = cap + 1  # cap too small, need more capacity

        return res