class MinStack:

    def __init__(self):
        self.arr=list()
    def push(self, val: int) -> None:
        self.arr.append(val)
        return self.arr
    def pop(self) -> None:
        self.arr.pop()
        return self.arr
    def top(self) -> int:
        top=0
        top=self.arr[len(self.arr)-1]
        return top
    def getMin(self) -> int:
        return(min(self.arr))
