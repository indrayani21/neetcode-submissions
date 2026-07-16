class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        max_values=max(freq.values())
        count=0
        for j in freq.values():
            if j==max_values:
                count+=1
        time=max(len(tasks),(max_values-1)*(n+1)+count)
        return time