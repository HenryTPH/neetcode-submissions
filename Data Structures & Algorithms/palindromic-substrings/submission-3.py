class Solution:
    def countSubstrings(self, s: str) -> int:
        # Manacher solution to study
        # 1. Convert s to t
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        P = [0] * n 
        C = 0 # Center of palindrome
        R = 0

        # 2. Scan each character in t
        for i in range(1, n - 1):
            # Mirror position of i by C
            i_mirror = 2 * C - i

            # If i in R, use i_mirror
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            
            # Expand around i if possible
            while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
                P[i] += 1

            # Update C and R if palindrome at i exceed R
            if i + P[i] > R:
                C = i
                R = i + P[i]

        return sum((v + 1) // 2 for v in P) 