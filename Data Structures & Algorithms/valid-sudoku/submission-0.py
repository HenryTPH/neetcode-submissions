class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Valid row is the easiest
        for row in board:
            check_dup = set()
            for str in row:
                if str != ".":
                    if str in check_dup:
                        return False
                    check_dup.add(str)

        # Valid column
        N = len(board)
        for i in range(N):
            check_dup = set()
            for j in range(N):                
                if board[j][i] != ".":
                    if board[j][i] in check_dup:
                        return False
                    check_dup.add(board[j][i])

        # Valid square        
        for bRow in range(0, 9, 3):
            for bCol in range(0, 9, 3):
                check_dup = set()
                for row in range(bRow, bRow + 3):
                    for col in range(bCol, bCol + 3):
                        if board[row][col] != ".":
                            if board[row][col] in check_dup:
                                return False
                            check_dup.add(board[row][col])
        return True