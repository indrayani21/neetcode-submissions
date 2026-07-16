class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output=[]
        for i in range(0,rowIndex+1):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=output[i-1][j-1]+output[i-1][j]
            output.append(row)
        return output[rowIndex]
        
        