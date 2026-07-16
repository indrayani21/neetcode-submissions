class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)     # userId -> list of (time, tweetId)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxheap = []
        
        # include self + followees
        users = self.following[userId] | {userId}
        
        for u in users:
            if self.tweets[u]:
                time, tweetId = self.tweets[u][-1]
                idx = len(self.tweets[u]) - 1
                heapq.heappush(maxheap, (-time, tweetId, u, idx))
        
        while maxheap and len(res) < 10:
            time, tweetId, u, idx = heapq.heappop(maxheap)
            res.append(tweetId)
            
            if idx > 0:
                time, tweetId = self.tweets[u][idx - 1]
                heapq.heappush(maxheap, (-time, tweetId, u, idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
