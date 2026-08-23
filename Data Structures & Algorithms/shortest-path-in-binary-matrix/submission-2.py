class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if not grid or grid[0][0] == 1 or grid[rows - 1][cols - 1]:
            return -1
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        def bfs(r, c, distant) -> int:
            queue = deque([(r, c, distant)])
            visited = {(r, c)}
            while queue:
                cr, cc, c_distant = queue.popleft()
                if cr == rows - 1 and cc == cols - 1:
                    return c_distant
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, c_distant + 1))
            
            return -1

        return bfs(0, 0, 1)