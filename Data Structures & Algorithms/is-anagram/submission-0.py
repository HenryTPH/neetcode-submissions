class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = dict()
        for c in s:
            if c not in my_dict:
                my_dict[c] = 1
            else:
                my_dict[c] += 1
        for c in t:
            if c in my_dict:
                my_dict[c] -= 1
                if my_dict[c] == 0:
                    my_dict.pop(c)
            else:
                return False
        return not my_dict