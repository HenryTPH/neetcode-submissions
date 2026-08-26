class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        count = 0
        longest = 0
        for num in table:
            if num - 1 not in table:
                count = 1
                while num + 1 in table:
                    count += 1
                    num += 1
                longest = max(longest, count)
                count = 0
        return longest