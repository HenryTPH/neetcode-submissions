class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        count = 0

        for num in set_num:
            if (num + 1) not in set_num:
                current_num = num
                current_count = 1

                while (current_num - 1) in set_num:
                    current_count += 1
                    current_num -= 1
                count = max(count, current_count)
        return count