class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[]
        if len(prices)<2:
            return 0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                p=prices[j]-prices[i]
                profit.append(p)
        for i in range(0,len(profit)):
            if profit[i]<0:
                if i==len(profit)-1:
                    return 0
            else:
                return max(profit)