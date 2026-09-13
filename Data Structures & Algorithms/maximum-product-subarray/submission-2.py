class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        cur_max, cur_min = nums[0], nums[0]

        for i in range(1, n):
            pre_max = cur_max
            pre_min = cur_min
            cur_max = max(nums[i], nums[i] * pre_max, nums[i] * pre_min)
            cur_min = min(nums[i], nums[i] * pre_max, nums[i] * pre_min)
            res = max(cur_max, res)
        return res