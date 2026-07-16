class WordDictionary:

    def __init__(self):
        self.arr=[]

    def addWord(self, word: str) -> None:
        self.arr.append(word)

    def search(self, word: str) -> bool:
        for w in self.arr:
            if len(w) != len(word):
                continue
            
            match = True
            
            for i in range(len(word)):
                if word[i] != '.' and word[i] != w[i]:
                    match = False
                    break
            
            if match:
                return True
        
        return False