class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        window = {}
        maxlen = 0
        
        for right in range(n):
            c = s[right]
            window[c] = window.setdefault(c, 0) + 1

            while window[c] > 1:
                left_c = s[left]
                window[left_c] -= 1
                if window[left_c] == 0:
                    del window[left_c]
                left += 1
            
            maxlen = max(maxlen, right - left + 1)
        return maxlen