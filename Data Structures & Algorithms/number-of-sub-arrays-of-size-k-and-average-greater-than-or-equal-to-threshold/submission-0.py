class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        sum = 0
        count = 0
        for right in range(len(arr)):
            sum += arr[right]
            if right - left + 1 == k:
                avg = sum / k
                if avg >= threshold:
                    count += 1
                sum -= arr[left]
                left += 1
        return count