class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rots = deque([])
        fresh = 0
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rots.append((r, c))
        if fresh == 0:
            return 0
        if not rots:
            return -1

        def bfs() -> bool:
            nonlocal fresh
            n = len(rots)
            rotted_fresh = False
            for _ in range(n):
                cur_r, cur_c = rots.popleft()
                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rots.append((nr, nc))
                        rotted_fresh = True
            return rotted_fresh

        while rots:
            if bfs():
                minutes += 1
        
        return -1 if fresh > 0 else minutes
