class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = end
        while start <= end:
            mid = start + (end - start) // 2
            total_hours = sum((e + mid - 1) // mid for e in piles)
            if total_hours > h:
                start = mid + 1
            else:
                end = mid - 1
                res = min(res, mid)
        return res