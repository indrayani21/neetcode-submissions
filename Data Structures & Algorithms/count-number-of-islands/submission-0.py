class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = "0"    # mark visited

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # valid land check
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"   # mark visited
                        queue.append((nx, ny))

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":       # found new island
                    bfs(i, j)
                    islands += 1

        return islands
