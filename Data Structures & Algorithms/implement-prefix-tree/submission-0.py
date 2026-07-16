class PrefixTree:

    def __init__(self):
        self.arr=[]

    def insert(self, word: str) -> None:
        self.arr.append(word)

    def search(self, word: str) -> bool:
        return word in self.arr

    def startsWith(self, prefix: str) -> bool:
        for i in self.arr:
            if i.startswith(prefix):
                return True
        return False
        