class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = [] # decreasing order
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while monotonic_stack and t > monotonic_stack[-1][0]:

                temp = monotonic_stack.pop()

                output[temp[1]] = i - temp[1]

            monotonic_stack.append([t, i])
        
        return output

        