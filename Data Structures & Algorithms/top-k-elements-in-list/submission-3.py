class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hash_table = dict()
        # Create a table of frequency
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
        # Buckets: index = frequency, value = list of numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in hash_table.items():
            buckets[value].append(key)
        # Traverse buckets from highest frequency to lowest
        for i in range(len(buckets) - 1, 0, -1):
            for element in buckets[i]:
                result.append(element)
                if len(result) == k:
                    return result
        return result