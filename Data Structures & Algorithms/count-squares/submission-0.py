class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for (px, py), freq in list(self.points.items()):
            if px == x and py != y:
                side = abs(py - y)

                # right square
                res += freq * self.points[(x + side, y)] * self.points[(x + side, py)]

                # left square
                res += freq * self.points[(x - side, y)] * self.points[(x - side, py)]

        return res