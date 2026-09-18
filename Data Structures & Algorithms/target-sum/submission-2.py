class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)

        def dp(i: int, current: int) -> int:
            if i == n:
                return 1 if current == target else 0
            if (i, current) in memo:
                return memo[(i, current)]
            memo[(i, current)] = dp(i + 1, current - nums[i]) + dp(i + 1, current + nums[i])
            return memo[(i, current)]

        return dp(0, 0)