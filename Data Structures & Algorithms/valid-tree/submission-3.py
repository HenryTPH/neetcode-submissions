class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parent[root_u] = root_v
            if root_u == root_v:
                return False
        return True