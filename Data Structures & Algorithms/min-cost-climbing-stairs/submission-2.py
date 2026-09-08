class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Bottom-up with dp table
        dp = [0 for _ in range(n + 1)]
        # Set starting points - base cases
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            # At position i, 1st choice is come from i - 1 and pay cost i - 1 with min cost at dp[i-1]. The second choice is from i - 2.
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        
        print(dp)
        return dp[n]