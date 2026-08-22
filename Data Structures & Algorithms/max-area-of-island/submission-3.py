class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        def bfs(r, c) -> int:
            queue = deque([(r, c)])
            grid[r][c] = 0
            area = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                cur_r, cur_c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = dr + cur_r, dc + cur_c
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = 0
                        area += 1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        return max_area

    