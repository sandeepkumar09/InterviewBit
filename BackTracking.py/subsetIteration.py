class Solution:
    # @param A: list of integers
    # @return a list of list of intergers
    def subsets(self, A):
        A.sort(reverse = True)
        results = [[]]
        while A:
            n = A.pop()
            temp = []
            for result in results:
                temp.append(result + [])
                temp.append(result + [n])
            results = temp
        results.sort()
        return results
sol = Solution()
print(sol.subsets([1,2]))
