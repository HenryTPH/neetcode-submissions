class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # At each number, we have 2 choices: 1 is add it to the subarray and calculate the sum, and 2 is start over the subarray at it.
        sub_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            sub_sum = max(num, sub_sum + num)
            max_sum = max(max_sum, sub_sum)    
        return max_sum