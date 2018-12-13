class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        hashmap = {}
        res = []
        if len(B) == 0:
            return []
        x = len(B[0])
        j = 0
        for i in range(x*len(B)-1, len(A)):
            word = A[j: i+1]
            print(i)
            print('word', word)
            start = j
            hashmap = {}
            for k in range(len(B)):
                wor = A[start: start+x]
                print('wor',wor)
                start += x
                if wor in hashmap:
                    hashmap[wor] += 1
                else:
                    hashmap[wor] = 1
            print(hashmap, i)
            for k in range(len(B)):
                if B[k] in hashmap:
                    hashmap[B[k]] -= 1
                    if hashmap[B[k]] < 0:
                        break
                else:
                	break
            else:
                res.append(j)
                print('res', res)
            print(hashmap, i)
            j += 1
        print(res)
        return res


sol = Solution()
print(sol.findSubstring('aaaa', ['a','a']))