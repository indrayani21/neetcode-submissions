class MyHashMap:

    def __init__(self):
        self.size=1000
        self.bucket=[[] for _ in range(self.size)]

    def hash(self,key):
        return key%self.size

    def put(self, key: int, value: int) -> None:
        idx=self.hash(key)
        for i, (k,v) in enumerate(self.bucket[idx]):
            if k==key:
                self.bucket[idx][i]=((key,value))
                return
        self.bucket[idx].append((key,value))
    def get(self, key: int) -> int:
        idx=self.hash(key)
        for k, v in self.bucket[idx]:
            if k == key:
                return v
        
        return -1

    def remove(self, key: int) -> None:
        idx=self.hash(key)
        for i, (k,v) in enumerate(self.bucket[idx]):
            if k==key:
                self.bucket[idx].pop(i)
                return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)