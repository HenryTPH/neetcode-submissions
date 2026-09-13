class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        rs_len = 0
        rs_start = 0
        
        def center_expand(left: int, right: int):
            nonlocal rs_len, rs_start
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            curr_len = right - left - 1 # Adjust right - 1 and left + 1
            if curr_len > rs_len:
                rs_start = left + 1
                rs_len = curr_len
            
        for i in range(n):
            center_expand(i, i)
            center_expand(i, i + 1)
        
        return s[rs_start: rs_start + rs_len]