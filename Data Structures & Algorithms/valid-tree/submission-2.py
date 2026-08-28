class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = deque([0])
        visited = {0}
        while queue:
            current = queue.popleft()
            for node in graph[current]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)

        return len(visited) == n