class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monotonic_stack = []

        for i, temp in enumerate(temperatures):
            while monotonic_stack and temperatures[monotonic_stack[-1]] < temp:
                poped_elem = monotonic_stack.pop()
                res[poped_elem] = i - poped_elem

            monotonic_stack.append(i)
        
        return res


        



        