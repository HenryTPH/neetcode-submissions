class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1
            if table[num] > 1:
                return True
        return False