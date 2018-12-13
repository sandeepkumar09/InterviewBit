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
    	#new_interval = list(new_interval)
    	start = new_interval[0]
    	end = new_interval[1]
    	return_intervals = []
    	for i in range(len(intervals)):
    		if intervals[i][1] < new_interval[0]:
    			return_intervals.append(intervals[i])
    		elif intervals[i][0] > new_interval[1]:
    			if s_flag == 1:
    				return_intervals.append((start, end))
    				s_flag = 0
    			return_intervals.append(intervals[i])
    		else:
    			s_flag = 1
    			if intervals[i][0] <= new_interval[0] and intervals[i][1] >= new_interval[0]:
    				start = intervals[i][0]
    			if intervals[i][0] <= new_interval[1] and intervals[i][1] >= new_interval[1]:
    				end = intervals[i][1]
    	return return_intervals
sol = Solution()
print(sol.insert( [(1, 3), (6, 9)],(2,5)))