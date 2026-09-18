class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for tar in range(target, num - 1, -1):
                if tar - num > 0:
                    dp[tar] = dp[tar - num] or dp[tar]
                elif tar - num == 0:
                    dp[tar] = True
                else:
                    dp[tar] = False
        return dp[target]

        