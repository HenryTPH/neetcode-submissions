class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1 # Shrink the matrix
        path = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        while queue:
            cr, cc, dis = queue.popleft()
            if cr == n - 1 and cc == n - 1:
                return dis
            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dis + 1))
        return -1