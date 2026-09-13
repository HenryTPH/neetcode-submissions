class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher algorithm
        t = "$#" + "#".join(s) + "#%"
        n = len(t)
        p = [0 for _ in range(n)]
        center = 0
        right = 0

        for i in range(1, n - 1):
            if i < right:
                j = 2 * center - i
                p[i] = min(right - i, p[j])
            else: 
                p[i] = 0
            while t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > right:
                center = i
                right = i + p[i]
        max_len, max_center = max((l, c) for c, l in enumerate(p))
        start_pos = (max_center - max_len) // 2
        return s[start_pos: start_pos + max_len]
