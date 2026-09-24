class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        memo = {}

        def dp(i: int, current: int) -> int:
            if current > target:
                return 0
            if i == len(stones):
                return current
            if (i, current) in memo:
                return memo[(i, current)]
            memo[(i, current)] = max(dp(i + 1, current), dp(i + 1, current + stones[i]))
            return memo[(i, current)]
        
        sub_max = dp(0, 0)
        return total - 2 * sub_max