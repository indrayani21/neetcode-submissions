class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n
        
        actual_sum = 0
        actual_sq_sum = 0
        
        for row in grid:
            for num in row:
                actual_sum += num
                actual_sq_sum += num * num
        
        expected_sum = N * (N + 1) // 2
        expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6
        
        diff = actual_sum - expected_sum          # x - y
        sq_diff = actual_sq_sum - expected_sq_sum # x² - y²
        
        sum_xy = sq_diff // diff                  # x + y
        
        x = (diff + sum_xy) // 2   # repeated
        y = sum_xy - x             # missing
        
        return [x, y]