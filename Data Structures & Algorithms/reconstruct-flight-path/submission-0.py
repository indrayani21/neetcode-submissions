class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        for u,v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort(reverse=True)
        res=[]
        def dfs(node):
            while graph[node]:
                nei=graph[node].pop()
                dfs(nei)
            res.append(node)
        dfs("JFK")
        return res[::-1]
