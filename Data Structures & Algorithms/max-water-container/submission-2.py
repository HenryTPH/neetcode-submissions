class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = float('-inf')
        for i in range(len(heights)):
            height_min = min(heights[left], heights[right])
            area = height_min * (right - left)
            if heights[left] < heights[right]:
                left += 1
            else: right -= 1
            max_area = max(area, max_area)
        return max_area
