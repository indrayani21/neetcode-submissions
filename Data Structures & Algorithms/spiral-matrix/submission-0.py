class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse top row (left to right)
            for i in range(left, right + 1):
                a.append(matrix[top][i])
            top += 1

            # Traverse right column (top to bottom)
            for i in range(top, bottom + 1):
                a.append(matrix[i][right])
            right -= 1

            # Traverse bottom row (right to left)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    a.append(matrix[bottom][i])
                bottom -= 1

            # Traverse left column (bottom to top)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    a.append(matrix[i][left])
                left += 1

        return a
                    