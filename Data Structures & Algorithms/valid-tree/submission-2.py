class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        queue=deque()
        queue.append((0,-1))
        visited.add(0)
        while queue:
            node,parent=queue.popleft()
            for nei in graph[node]:
                if nei==parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                queue.append((nei,node))
        return len(visited)==n