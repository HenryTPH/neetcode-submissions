class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i] = The minimum number of coins needed to make amount i
        The target is amount => the array size must be amount + 1
        """
        dp = [float("inf") for _ in range(amount + 1)]

        # Base case: To make amount of 0, we need 0 coins
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a >= coin:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return dp[amount] if dp[amount] != float("inf") else -1

        
