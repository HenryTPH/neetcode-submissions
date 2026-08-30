class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(money):
            # Base case:
            if money == 0:
                return 0
            if money < 0:
                return float("inf")
            
            if money in memo:
                return memo[money]
            
            min_coins = float("inf")
            for coin in coins:
                res = dfs(money - coin)
                min_coins = min(min_coins, 1 + res)
            memo[money] = min_coins
            return memo[money]
        rs = dfs(amount)
        return rs if rs != float("inf") else -1
            