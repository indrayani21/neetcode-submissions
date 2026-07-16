class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def combsum(remaining,comb,start):
            if remaining==0:
                res.append(list(comb))
                return
            elif remaining<0:
                return 
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remaining:
                    break
                comb.append(candidates[i])
                combsum(remaining-candidates[i],comb,i+1)
                comb.pop()
        combsum(target,[],0)
        return res