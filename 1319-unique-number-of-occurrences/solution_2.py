# https://leetcode.com/problems/unique-number-of-occurrences
# https://leetcode.com/problems/1319-unique-number-of-occurrences
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return len(set(d.values()))==len(d.values())
