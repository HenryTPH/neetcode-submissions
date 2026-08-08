class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Complexity should be O(n) in time and O(1) in space
        buy = float('inf')
        profit = 0

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit