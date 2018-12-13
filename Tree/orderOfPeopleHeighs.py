class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
    	hashmap = {}
    	arr = []
    	ans = [-1]*len(A)
    	sort_height = []
    	for i in range(len(A)):
    		arr.append(i)
    		hashmap[A[i]] = B[i]
    		sort_height.append(A[i])
    	sort_height.sort()

    	for i in range(len(A)):
    		ele = sort_height[i]
    		position = hashmap[ele]
    		k = arr[position]
    		ans[k] = ele
    		del(arr[position])
    	return ans
sol = Solution()
print(sol.order([5,3,2,6,1,4], [0,1,2,0,3,2]))