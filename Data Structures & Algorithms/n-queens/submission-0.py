class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path=[]
        board = [["." for _ in range(n)] for _ in range(n)]
        def issafe(board,row,col):
            #horizontal
            for j in range(0,n):
                if board[row][j]=="Q":
                    return False
            #vertical
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True
        def nqueens(board,row):
            if row == n:
                path.append(["".join(r) for r in board])
                return

            for j in range(n):
                if issafe(board, row, j):
                    board[row][j] = "Q"
                    nqueens(board, row + 1)
                    board[row][j] = "."

        nqueens(board, 0)
        return path