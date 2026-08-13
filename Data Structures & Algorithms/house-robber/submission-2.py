class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        base_1 = nums[0]
        base_2 = nums[1]
        max_dp_before_previous = base_1
        for i in range(2, len(nums)):
            current = max_dp_before_previous + nums[i]
            max_dp_before_previous = max(max_dp_before_previous, base_2)
            base_1 = base_2
            base_2 = current
        return max(base_2, base_1)