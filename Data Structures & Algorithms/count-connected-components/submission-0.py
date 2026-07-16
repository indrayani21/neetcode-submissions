class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
    
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        components = 0
        
        def dfs(node):
            for nei in graph[node]:
                if not visited[nei]:   # ✅ FIXED
                    visited[nei] = True
                    dfs(nei)
        
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                components += 1
        
        return components