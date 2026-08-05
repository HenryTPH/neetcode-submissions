class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        store_value = [0] * (n + 1)
        store_value[1] = 1
        store_value[2] = 2

        for i in range(3, n + 1):
            store_value[i] = store_value[i - 1] + store_value[i - 2]
        return store_value[n]