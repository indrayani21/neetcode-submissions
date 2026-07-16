class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st=set(wordList)
        q=deque()
        q.append([beginWord])
        usedonLevel=[beginWord]
        level=0
        while q:
            vec=q.popleft()
            if len(vec)>level:
                level+=1
                for word in usedonLevel:
                    if word in st:
                        st.remove(word)
                usedonLevel=[]
            word=vec[-1]
            if word==endWord:
                return len(vec)
            for i in range(0,len(word)):
                orginal=word[i]
                for c in range(ord("a"), ord("z")+1):
                    new_word=chr(c)
                    word_List=list(word)
                    word_List[i]=new_word
                    new_word="".join(word_List)
                    if new_word in st:
                        vec.append(new_word) 
                        q.append(list(vec)) 
                        usedonLevel.append(new_word) 
                        vec.pop()
        return 0
