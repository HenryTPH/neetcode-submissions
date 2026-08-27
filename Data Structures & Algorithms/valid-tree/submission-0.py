class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(i: int):
            visited.add(i)
            for node in graph[i]:
                if node not in visited:
                    dfs(node)

        dfs(0)
        return len(visited) == n