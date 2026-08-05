class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)

        # If the largest element is negative or the first element is positive, or the length of the array is less than 3, sum can never be 0
        if length < 3 or nums[-1] < 0 or nums[0] > 0:
            return []

        for i in range(length - 2):
            # Skip the duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, length - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move the pointer and skip duplicates for the left and the right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else: 
                    right -= 1
        return result