class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            node=queue.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return len(topo)==numCourses