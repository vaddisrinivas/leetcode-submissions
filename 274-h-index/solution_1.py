# https://leetcode.com/problems/h-index
# https://leetcode.com/problems/274-h-index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if len(citations)==1: return 1 if citations[0] else 0
        if sum(citations)==0: return 0
        flag = False
        for i in range(len(citations)):
            if i+1>citations[i]:
                flag = True
                break
        return i if flag else len(citations)