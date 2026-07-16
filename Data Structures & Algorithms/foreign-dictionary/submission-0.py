class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def topologicalsort(graph,indegree):
            queue=deque()
            for ch in indegree:
                if indegree[ch]==0:
                    queue.append(ch)
            topo=[]
            while queue:
                node=queue.popleft()
                topo.append(node)
                for nei in graph[node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        queue.append(nei)
            return topo
        graph=defaultdict(list)
        indegree={}
        # intialize all characters
        for word in words:
            for ch in word:
                indegree[ch]=0
        for i in range(0,len(words)-1,1):
            s1,s2=words[i],words[i+1]
            #prefix case:
            if len(s1)>len(s2) and s1.startswith(s2):
                return ""
            size=min(len(s1),len(s2))
            for j in range(0,size):
                if s1[j]!=s2[j]:
                    graph[s1[j]].append(s2[j])
                    indegree[s2[j]]+=1
                    break
        topo=topologicalsort(graph,indegree)
        if len(topo)==len(indegree):
            return "".join(topo)
        return ""        