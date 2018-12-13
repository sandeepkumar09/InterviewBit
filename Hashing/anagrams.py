class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):

        hashmap = {}
        for index, word in enumerate(A):
            # Sorted returns a list convert it to a string
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [index+1]
            else:
                # Appending the next index to list associated with key
                hashmap[sorted_word] += [index+1]
        return list(hashmap.values())


sol = Solution()
print(sol.anagrams(["cat", "dog", "god", "tca"]))
