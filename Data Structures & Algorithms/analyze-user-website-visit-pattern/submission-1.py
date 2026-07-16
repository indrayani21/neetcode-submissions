class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: sort by time
        data = sorted(zip(username, timestamp, website), key=lambda x: x[1])
        
        # Step 2: group by user
        user_map = defaultdict(list)
        for u, t, w in data:
            user_map[u].append(w)
        
        # Step 3 & 4: generate patterns
        count = Counter()
        
        for user in user_map:
            websites = user_map[user]
            
            # unique sequences per user
            seen = set(combinations(websites, 3))
            
            for seq in seen:
                count[seq] += 1
        
        # Step 5: find best
        return list(min(count, key=lambda x: (-count[x], x)))