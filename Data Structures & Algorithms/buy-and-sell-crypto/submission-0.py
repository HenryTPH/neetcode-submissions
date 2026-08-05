class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        future_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                future_profit = max(profit, future_profit)
            else:
                left = right
            right += 1
        return future_profit