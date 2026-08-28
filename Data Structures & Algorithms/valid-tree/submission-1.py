class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {0}
        stack = [0]
        while stack:
            current = stack.pop()
            for node in graph[current]:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)
        return len(visited) == n