class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap= [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            a=-heapq.heappop(maxheap)
            b=-heapq.heappop(maxheap)
            if a != b:
                heapq.heappush(maxheap, -(a - b))
        return -maxheap[0] if maxheap else 0
