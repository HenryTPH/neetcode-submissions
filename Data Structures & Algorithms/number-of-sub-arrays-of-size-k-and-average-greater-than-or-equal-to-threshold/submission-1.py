class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current = sum(arr[:k])
        count = 1 if current / k >= threshold else 0
        for num in range(k, len(arr)):
            current += arr[num] - arr[num - k]
            
            if current/k >= threshold:
                count += 1
        return count