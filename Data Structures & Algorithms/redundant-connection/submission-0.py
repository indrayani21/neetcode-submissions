class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=list(range(len(edges)+1))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(u,v):
            pu,pv=find(u),find(v)
            if pu==pv: # cycle detected
                return False
            parent[pv]=pu
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        return []