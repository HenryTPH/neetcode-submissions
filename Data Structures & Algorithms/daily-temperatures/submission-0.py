class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for pos in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[pos]:
                curr = stack.pop()
                result[curr[1]] = pos - curr[1]

            stack.append((temperatures[pos], pos))
        return result