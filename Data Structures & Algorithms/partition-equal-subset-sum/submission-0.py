class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        def dp(i: int, target: int) -> bool:
            if target == 0:
                return True
            if target < 0:
                return False
            if i < 0:
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = dp(i - 1, target) or dp(i - 1, target - nums[i])
            return memo[(i, target)]
        
        return dp(len(nums) - 1, target)