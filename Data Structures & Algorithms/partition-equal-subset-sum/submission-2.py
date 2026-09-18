class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        memo = {}
        def dp(i: int, cur_sum: int) -> bool:
            if cur_sum == target:
                return True
            if cur_sum > target:
                return False
            if i == n:
                return False
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
            memo[(i, cur_sum)] = dp(i + 1, cur_sum + nums[i]) or dp(i + 1, cur_sum)
            return memo[(i, cur_sum)]

        return dp(0, 0)