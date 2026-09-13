class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        rs = nums[0]

        def dp(i: int) -> tuple[int, int]:
            if i == 0:
                memo[0] = (nums[0], nums[0])
                return (nums[0], nums[0])
            
            if i in memo:
                return memo[i]
            prev_max, prev_min = dp(i - 1)
            max_product = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            min_product = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            memo[i] = (max_product, min_product)
            return memo[i]
        
        for i in range(len(nums)):
            cur_max, _ = dp(i)
            rs = max(cur_max, rs)
        return rs