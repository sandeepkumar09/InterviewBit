class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
    	self.hashmap = {}
    	self.countStairs(A)
    	return self.hashmap[A]
    def countStairs(self, A):
    	if A in self.hashmap:
    		return self.hashmap[A]
    	count = 0
    	if A == 0:
    		return 1
    	elif A < 0:
    		return 0
    	else:
    		count += self.countStairs(A-1)
    		count += self.countStairs(A-2)
    	self.hashmap[A] = count
    	return count

sol = Solution()
print(sol.climbStairs(4))