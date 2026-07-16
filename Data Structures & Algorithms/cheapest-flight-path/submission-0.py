class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,pr in flights:
            graph[u].append((v,pr))
        pq=[(0,src,0)]
        visited=dict()
        while pq:
            cost,node,stop=heapq.heappop(pq)
            if node==dst:
                return cost
            if stop>k:
                continue
            if (node,stop) in visited and visited[(node,stop)]<=cost:
                continue
            visited[(node,stop)]=cost
            for nei,pr in graph[node]:
                heapq.heappush(pq,(cost+pr,nei,stop+1))
        return -1

        