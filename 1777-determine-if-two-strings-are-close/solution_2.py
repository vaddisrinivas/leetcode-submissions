# https://leetcode.com/problems/determine-if-two-strings-are-close
# https://leetcode.com/problems/1777-determine-if-two-strings-are-close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 , w2 = {}, {}
        for i in word1:
            if i in w1:
                w1[i] += 1
            else:
                w1[i]=1
        for i in word2:
            if i in w2:
                w2[i] += 1
            else:
                w2[i]=1
        if set(w1.keys())!=set(w2.keys()):
            return False
        if sorted(w1.values())!=sorted(w2.values()):
            return False
        for i in w2:
            if w2[i] not in w1.values():
                return False
        return True
        