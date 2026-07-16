class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def ispossible(r, c, mid, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                return False
            # ❌ cannot enter this cell yet
            if grid[r][c] > mid:
                return False
            # ✅ reached destination
            if r == rows - 1 and c == cols - 1:
                return True
            visited[r][c] = True
            # explore all 4 directions
            return (
                ispossible(r+1, c, mid, visited) or
                ispossible(r-1, c, mid, visited) or
                ispossible(r, c+1, mid, visited) or
                ispossible(r, c-1, mid, visited)
            )
        
        left = grid[0][0]
        right = rows * cols - 1
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            
            visited = [[False]*cols for _ in range(rows)]  # 🔥 reset every time
            
            if ispossible(0, 0, mid, visited):  # 🔥 start from (0,0)
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
