class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                pop_temp = stack.pop()
                days_waited = i - pop_temp[0]
                result[pop_temp[0]] = days_waited
            stack.append((i, temperatures[i]))
        return result