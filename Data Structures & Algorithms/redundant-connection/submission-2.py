class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)

        def bfs(u: int, v: int) -> bool:
            queue = deque([(u, -1)])
            visited = {u}

            while queue:
                current, parent = queue.popleft()
                if current == v:
                    return True
                for node in graph[current]:
                    if node == parent:
                        continue
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, current))
            return False

        for u, v in edges:
            if bfs(u, v):
                return [u, v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        return []