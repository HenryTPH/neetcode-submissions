class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_Area = 0
        while left < right:
            pos_diff = right - left
            height_min = min(heights[left], heights[right])
            area = pos_diff * height_min
            if area > max_Area:
                max_Area = area
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                if heights[left + 1] > heights[right - 1]:
                    left += 1
                elif heights[left + 1] < heights[right - 1]:
                    right -= 1
                else:
                    left += 1
                    right -= 1
        return max_Area