class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        length = len(nums) + 1
        total = 0

        for right in range(n):
            total += nums[right]
            while total >= target:
                length = min(length, right - left + 1)
                total -= nums[left]
                left += 1
        return length if length != len(nums) + 1 else 0
