class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] == "0"

            while queue:
                r_curr, c_curr = queue.popleft()

                for dr, dc in directions:
                    new_r, new_c = r_curr + dr, c_curr + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        grid[new_r][new_c] = "0"
                        queue.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands