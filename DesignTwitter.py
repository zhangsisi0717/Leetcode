from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.time = 0
        self.user_to_tweets = defaultdict(list)
        self.user_to_followee = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append([(-1)*self.time,tweetId,len(self.user_to_tweets[userId])])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ##heap [self.time,tweetId,list_idx]
        result=[]
        followee_tweet = [self.user_to_tweets[i][0] for i in self.user_to_followee[userId]]
        self_tweet =  [self.user_to_tweets[userId][0]]
        heap = followee_tweet + self_tweet
        print(f"heap={heap}")
        heapq.heapify(heap)
        print(f"heap after heaplify = {heap}")
        while (len(result)<10 and heap):
            result.append(heap[0][1])
            print(f"run here 1 heap = {heap}")
            if heap[0][2]+1 < len(self.user_to_tweets[heap[0][1]]):
                next_node = self.user_to_tweets[heap[0][1]][heap[0][2]+1]
                print(f"next_node = {next_node}")
                heapq.heapreplace(heap,next_node)
            else:
                print("run here")
                heapq.heappop(heap)
                print(f"heap after pop={heap}")
                print(f"bool(heap) = {bool(heap)}")

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_followee[followerId].add(followeeId)

        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.user_to_followee[followerId]:
            self.user_to_followee.pop(followerId)

t = Twitter()
t.postTweet(1,5)
t.getNewsFeed(1)
t.follow(1,2)
t.postTweet(2,6)


t.getNewsFeed(1)
t.unfollow(1,2)
t.getNewsFeed(1)

t.user_to_followee[1]
t.user_to_tweets[2]

# for i in t.user_to_followee[1]:
#     for j in t.user_to_tweets[i]:
#         print(j)