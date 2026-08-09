class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {c: s1.count(c) for c in s1}
        length = len(s1)
        left = 0
        right = length - 1
        sub_dict = {c: s2[0:length].count(c) for c in s2[0:length]}
        while right < len(s2):
            # Compare subdict and dict_s1
            if dict_s1 == sub_dict:
                return True
            else:
                sub_dict[s2[left]] -= 1
                if sub_dict[s2[left]] == 0:
                    sub_dict.pop(s2[left])
                left += 1
                right += 1
                if right < len(s2):
                    sub_dict[s2[right]] = sub_dict.get(s2[right], 0) + 1
        return False
        