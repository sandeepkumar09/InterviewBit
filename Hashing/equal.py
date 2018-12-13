class Solution:
    # @param A : list of integers
    # @return a list of integers

    def equal(self, A):
        ans = []
        hashmap = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i]+A[j] in hashmap:
                    a, b = hashmap[A[i]+A[j]]
                    if a < i and b != i and b != j:
                        ans.append(hashmap[A[i]+A[j]] + [i, j])
                else:
                    hashmap[A[i]+A[j]] = [i, j]
        if ans:
            ans.sort()
            return ans[0]
        return []


sol = Solution()
print(sol.equal([]))
