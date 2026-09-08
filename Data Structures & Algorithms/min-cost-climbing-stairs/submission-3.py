class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        table = {}

        def dp(i: int) -> int:
            # Base case, at step 0, and 1, cost is 0
            if i == 0 or i == 1:
                return 0
            
            if i in table:
                return table[i]
            table[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

            return table[i]
        return dp(n)