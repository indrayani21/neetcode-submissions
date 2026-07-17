class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[]
        for i in range(0,numRows):
            rows=[1]*(i+1)
            for j in range(1,i):
                rows[j]=output[i-1][j-1]+output[i-1][j]
            output.append(rows)
        return output