# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        ans,ins=[],0
        for ii in intervals: 
            i=[ii.start,ii.end] 
            if i[1]<new_interval.start: 
                ans.append(ii) 
            elif i[0]>new_interval.end: 
                if ins==0: 
                    ans.append(new_interval) 
                    ins=1 
                ans.append(ii) 
            else: 
                new_interval.start,new_interval.end=min(new_interval.start,i[0]),max(new_interval.end,i[1]) 
        if ins==0: 
            ans.append(new_interval) 
        return(ans)