class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=[]
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                if words[i] in words[j] and i!=j:
                    a.append(words[i])
        return list(set(a))