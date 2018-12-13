class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort(reverse = True)
        results = [[]]
        while A:
            n = A.pop()
            temp = []
            for result in results:
                temp.append(result+[])
                temp.append(result+[n])
            results = temp
        results.sort()
        temp = []
        for i,result in enumerate(results):
            if not temp or results[i] != temp[-1]:
                temp.append(result)
        return temp
sol = Solution()
print(sol.subsetsWithDup([1,1,2,2,2,2]))
