class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        queue=deque()
        def addroom(r,c):
            if r<0 or r==rows or c<0 or c==cols or (r,c) in visit or grid[r][c]==-1:
                return
            queue.append([r,c])
            visit.add((r,c))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    queue.append([i,j])
                    visit.add((i,j))
        dist=0
        while queue:
            for _ in range(len(queue)):
                r,c =queue.popleft()
                grid[r][c]=dist
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            dist+=1
