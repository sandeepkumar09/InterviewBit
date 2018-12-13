# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
    	print(intervals.sort())
    	new_intervals = []
    	for i in range(1,len(intervals)):
    		if intervals[i][0] <= intervals[i-1][1]:
    			new_intervals.append([intervals[i-1][0], intervals[i][1]])
    		else:
    			new_intervals.append(intervals[i])
    	return new_intervals
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))