class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        b=[]
        for i in range(0,n+1):
            if i==0:
                a.append(0)
            elif i==1:
                a.append(1)
            elif i>1:
                b=[]
                while i//2>=1:
                    d=i%2
                    b.append(d)
                    i=i//2
                b.append(1)
                b=b[::-1]
                a.append(b.count(1))
        return a