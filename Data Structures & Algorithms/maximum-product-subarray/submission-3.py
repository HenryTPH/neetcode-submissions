class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        suffix = 0
        max_product = float('-inf')

        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n - 1 - i]
            max_product = max(max_product, prefix, suffix)

        return max_product