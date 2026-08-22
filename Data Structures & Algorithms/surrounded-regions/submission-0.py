class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Edges cases
        if not board:
            return
        # Fist, we traverse through edge cells to find island and change them to "R" mean reserve.
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "R"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == "O":
                    dfs(r, c)

        # Now we will convert all "O" to "X" and "R" to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "R":
                    board[r][c] = "O"