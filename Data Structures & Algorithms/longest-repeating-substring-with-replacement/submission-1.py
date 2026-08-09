class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        table = dict()
        max_length = 0
        for i in range(len(s)):
            table[s[i]] = table.get(s[i], 0) + 1
            most_frequency_letter = max(table, key=table.get)
            replacements_possible = i - left + 1 - table[most_frequency_letter]
            while replacements_possible > k:
                table[s[left]] -= 1
                left += 1
                most_frequency_letter = max(table, key=table.get)
                replacements_possible = i - left + 1 - table[most_frequency_letter]
            
            max_length = max(i - left + 1, max_length)
        return max_length