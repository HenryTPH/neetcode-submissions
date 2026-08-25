class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
        visited = set()
        count = 0

        def dfs(city: int) -> None:
            if city in visited:
                return
            visited.add(city)
            neighbors = graph[city]
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                count += 1
                dfs(city)
        return count