class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != "O" or visited[r][c] == 1
            ):
                return
            
            visited[r][c] = 1
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        visited = [[0]*cols for _ in range(rows)]
        
        # Traverse borders
        for j in range(cols):
            if board[0][j] == "O" and visited[0][j] == 0:
                dfs(0, j)
            if board[rows-1][j] == "O" and visited[rows-1][j] == 0:
                dfs(rows-1, j)
        
        for i in range(rows):
            if board[i][0] == "O" and visited[i][0] == 0:
                dfs(i, 0)
            if board[i][cols-1] == "O" and visited[i][cols-1] == 0:
                dfs(i, cols-1)
        
        # Convert surrounded regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"