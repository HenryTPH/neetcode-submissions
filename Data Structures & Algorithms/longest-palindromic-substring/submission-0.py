class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        memo = {}
        start_point = 0
        max_len = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif j == i + 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    start_point = i
        
        return s[start_point: start_point + max_len]