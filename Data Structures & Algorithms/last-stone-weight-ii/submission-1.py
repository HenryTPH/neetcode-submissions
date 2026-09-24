class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for choice in range(target, stone - 1, -1):
                dp[choice] = dp[choice] or dp[choice - stone]

        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s
        return 0