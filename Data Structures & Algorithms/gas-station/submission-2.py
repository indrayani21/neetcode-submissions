class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank=0
        start_index=0
        if sum(gas)<sum(cost):
            return -1
        else:
            for i in range(0,len(gas)):
                tank+=gas[i]-cost[i]
                if tank<0:
                    start_index=i+1
                    tank=0
        return start_index