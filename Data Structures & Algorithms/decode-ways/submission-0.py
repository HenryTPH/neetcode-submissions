class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dp(i: int) -> int:
            if i == n:
                return 1
            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]
            
            s1 = dp(i + 1)
            s2 = dp(i + 2) if int(s[i:i + 2]) in range (10, 27) else 0
            memo[i] = s1 + s2

            return memo[i]
        
        return dp(0)