class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        cal = total + target
        if cal % 2 != 0 or total < abs(target):
            return 0
        sub_target =  cal // 2

        dp = [0] * (sub_target + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(sub_target, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]

        return dp[sub_target]