# https://leetcode.com/problems/edit-distance
# https://leetcode.com/problems/72-edit-distance
from copy import deepcopy
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # carrot
        # shred
        # t delete
        # o, r replace
        # c, a replace
        # pizza
        # pasta
        # i,z,z replace
        # sridhar
        # samrat
        # r replace 
        # h delete
        # rid replace
        # inen-tion
        # execution
        # free
        # reep
        # match length
        # common characters/sequences
        # minimal distance
        # ops = [None, None, None]
        # d = [ops for i in range(len(word2))]
        # d = [None]*len(word1)
        d = {}
        def dfs(n1,n2):
            if n1<len(word1) and n2<len(word2) and (n1,n2) in d:
                return d[(n1,n2)]
            while n2<len(word2) and n1<len(word1) and word1[n1]==word2[n2] :
                n1 += 1
                n2 += 1
            if (n1>=len(word1) and n2>=len(word2)):
                return 0
            elif n1>=len(word1) and n2<len(word2):
                return len(word2)-n2
            elif n1<len(word1) and n2>=len(word2):
                return len(word1)-n1
            c = 0
            # insert 
            c0 = dfs(n1,n2+1)+1
            # delete
            c1 = dfs(n1+1,n2)+1
            # replace
            c2 = dfs(n1+1,n2+1)+1
            d[(n1,n2)]=min(c0,c1,c2)
            return d[(n1,n2)]
            # return min(c0,c1,c2)
        return dfs(0,0)