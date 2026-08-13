class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if len(nums) == 2:
            return [nums[1], nums[0]]
        prefix = [1] * len(nums)
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = 1
        for j in range(n - 1, -1, -1):
            prefix[j] = prefix[j] * postfix
            postfix *= nums[j]
        return prefix