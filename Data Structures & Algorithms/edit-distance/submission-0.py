class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return 0
            if i == 0:
                return j
            if j == 0:
                return i
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i - 1] == word2[j - 1]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = 1 + min(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1))
            return memo[(i, j)]

        return dp(len(word1), len(word2))