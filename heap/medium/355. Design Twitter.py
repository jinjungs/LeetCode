from collections import defaultdict
import heapq
import time
from typing import List

class Twitter:
    def __init__(self):
        self.tweets     = defaultdict(list) # key: userId, value: heap of 10 (time, tweetId)
        self.follows    = defaultdict(set) # key: followerId, value: set of followeeId 

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (time.time(), tweetId))
        if len(self.tweets[userId]) > 10:
            heapq.heappop(self.tweets[userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows[userId]
        followees.add(userId)
        
        q = []
        for followee in followees:
            q.extend([(-x[0], x[1]) for x in self.tweets[followee]])
        heapq.heapify(q)

        news = []
        n = 10
        while q and n > 0:
            t, tweet = heapq.heappop(q)
            news.append(tweet)
            n -= 1
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)