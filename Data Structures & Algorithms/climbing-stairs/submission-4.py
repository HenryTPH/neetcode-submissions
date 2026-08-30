class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(steps):
            if steps == 0:
                return 1
            if steps < 0:
                return 0
            if steps in memo:
                return memo[steps]
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)

            return memo[steps]
        return dfs(n)