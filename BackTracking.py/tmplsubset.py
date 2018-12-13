class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort(reverse=True)
        results = [[]]
        while A:
            n = A.pop()
            temp = []
            for result in results:
                temp.append(result + [])
                temp.append(result + [n])
            results = temp
        print(results)
        results.sort()
        return results


sol = Solution()
#print(sol.subsets( [ 15, 20, 12, 19, 4 ]))
print(sol.subsets([1,2,3,4]))
