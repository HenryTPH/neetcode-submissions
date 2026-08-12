class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        previous_1, previous_2 = 1, 2

        for i in range(3, n + 1):
            current = previous_1 + previous_2
            previous_1 = previous_2
            previous_2 = current

        return previous_2