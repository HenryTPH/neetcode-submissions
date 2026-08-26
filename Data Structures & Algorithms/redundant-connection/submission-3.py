class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)        

        def dfs(u: int, v: int) -> bool:
            if u == v:
                return True
            visited.add(u)
            for node in graph[u]:
                if node not in visited:
                    visited.add(node)   
                    if dfs(node, v):
                        return True
            return False

        for u, v in edges:
            visited = set()
            if dfs(u, v):
                return [u, v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        return []