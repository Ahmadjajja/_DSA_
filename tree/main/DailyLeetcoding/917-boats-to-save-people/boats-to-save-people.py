class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # nlogn

        left = 0
        right = len(people) - 1
        countBoats = 0

        # [1, 2, 2, 3], 3 => 3

        while left <= right:

            sum = people[left] + people[right]
            if sum <= limit:
                countBoats += 1
                left += 1
                right -= 1
            else:
                countBoats += 1
                right -= 1
        
        return countBoats
        


        