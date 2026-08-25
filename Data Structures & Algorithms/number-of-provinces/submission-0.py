class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = {}
        for i in range(n):
            graph[i] = []
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
        visited = set()
        count = 0

        def bfs(city: int) -> None:
            queue = deque([city])
            visited.add(city)
            while queue:
                current_city = queue.popleft()
                for neighbor in graph[current_city]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)

        return count