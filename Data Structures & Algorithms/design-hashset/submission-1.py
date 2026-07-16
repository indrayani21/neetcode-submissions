class MyHashSet:

    def __init__(self):
        self.size=1000
        self.bucket=[[] for _ in range(self.size)]

    def hash(self,key):
        return key%self.size # where our key goes

    def add(self, key: int) -> None:
        idx=self.hash(key)
        if key not in self.bucket[idx]:
            self.bucket[idx].append(key)

    def remove(self, key: int) -> None:
        idx=self.hash(key)
        if key in self.bucket[idx]:
            self.bucket[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx=self.hash(key)
        return key in self.bucket[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)