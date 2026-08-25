class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j) -> List[int]:
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return [i, j]
            parent[root_i] = root_j
            return []

        for u, v in edges:
            uf = union(u, v)
            if uf:
                return uf
        return []