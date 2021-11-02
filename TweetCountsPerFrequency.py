#https://leetcode.com/problems/tweet-counts-per-frequency/
from type_checking import *
from collections import defaultdict
class TweetCounts:

    def __init__(self):

        ##name_to_frequence = {Tweetname:{hour:{0:[0,10]}, minite:{0:[0]},second:{0,[0]}}}
        f = lambda: defaultdict(f)
        self.name_to_time = defaultdict(list)
        self.freq_to_num = {"minute":60,"hour":3600,"day":86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.name_to_time[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        fre_num = self.freq_to_num[freq]
        num_inter = (endTime-startTime) // fre_num
        result = [0 for _ in range(num_inter+1)]
        for t in self.name_to_time[tweetName]:
            if t<startTime or t>endTime:continue
            index = (t - startTime) // fre_num
            if index < len(result):
                result[index] +=1

        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)