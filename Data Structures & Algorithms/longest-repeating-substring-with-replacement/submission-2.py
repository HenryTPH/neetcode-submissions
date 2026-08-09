class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        table = dict()
        max_length = most_frequency_letter = 0
        for i in range(len(s)):
            table[s[i]] = table.get(s[i], 0) + 1
            most_frequency_letter = max(most_frequency_letter, table[s[i]])            
            while i - left + 1 - most_frequency_letter > k:
                table[s[left]] -= 1
                left += 1
            
            max_length = max(i - left + 1, max_length)
        return max_length