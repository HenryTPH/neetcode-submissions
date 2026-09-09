class Solution:
    def numDecodings(self, s: str) -> int:
        # Dp the number of ways to decode the substring at index i
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            state_1 = dp[i + 1] if s[i] != '0' else 0
            state_2 = dp[i + 2] if s[i] != '0' and int(s[i:i+2]) in range(10, 27) else 0
            dp[i] = state_1 + state_2
        return dp[0]
            