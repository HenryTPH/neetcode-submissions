class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}

        for letter in s:
            table[letter] = table.get(letter, 0) + 1

        for c in t:
            if c in table:
                table[c] -= 1
            else: 
                return False
            if table[c] == 0:
                table.pop(c)
        
        return not table