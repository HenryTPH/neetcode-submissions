class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            remain = target - nums[i]

            if remain in table:
                return [table[remain], i]
            
            table[num] = i
        return []
