class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        total = sum(nums)
        cal = total + target
        if cal % 2 != 0 or total < abs(target):
            return 0
        sub_target =  cal // 2

        def dp(i: int, current: int) -> int:
            if current > sub_target:
                return 0
            if i == len(nums):
                return 1 if current == sub_target else 0
            
            if (i, current) in memo:
                return memo[(i, current)]
            memo[(i, current)] = dp(i + 1, current) + dp(i + 1, current + nums[i])
            return memo[(i, current)]
        
        return dp(0, 0)