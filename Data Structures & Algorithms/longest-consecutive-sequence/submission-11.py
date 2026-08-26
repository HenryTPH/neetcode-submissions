class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        parent = {num : num for num in nums}
        size = {num: 1 for num in nums}

        def find(num: int) -> int:
            if parent[num] == num:
                return num
            parent[num] = find(parent[num])
            return parent[num]

        def union(u: int, v: int):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parent[root_u] = root_v
                size[root_v] += size[root_u]

        for num in parent:
            if num + 1 in parent:
                union(num, num + 1)

        return max(size.values())