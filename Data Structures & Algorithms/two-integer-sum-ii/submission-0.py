class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            num_left = numbers[left]
            num_right = numbers[right]
            if num_left + num_right > target:
                right -= 1
                continue
            if num_left + num_right < target:
                left += 1
                continue
            if num_left + num_right == target:
                return [left + 1, right + 1]
        return[left + 1, right + 1]