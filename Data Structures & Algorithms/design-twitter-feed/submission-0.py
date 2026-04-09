import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.count = 0  # Global timer to track tweet order
        self.tweet_map = defaultdict(list)  # userId -> list of [count, tweetId]
        self.follow_map = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Use negative count for the min-heap to act as a max-heap
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []

        # A user always follows themselves
        self.follow_map[userId].add(userId)
        
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                # Push (count, tweetId, followeeId, index - 1)
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                next_count, next_tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [next_count, next_tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
