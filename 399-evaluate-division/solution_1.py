# https://leetcode.com/problems/evaluate-division
# https://leetcode.com/problems/399-evaluate-division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        inc = 0
        out = 1
        for i,j in enumerate(equations):
            if j[inc] in d:
                d[j[inc]].update({j[out]:values[i]})
            else:
                d[j[inc]] = {j[out]:values[i]}
            if j[out] in d:
                d[j[out]].update({j[inc]:1/values[i] if values[i]!=0 else -1})
            else:
                d[j[out]] = {j[inc]:1/values[i] if values[i]!=0 else -1}
        res = []

        def cd(curr, target,visited,prod=1):
            nonlocal d
            if target in d[curr]:
                return prod*d[curr][target]
            res = None
            for i in d[curr]:
                if i not in visited:
                    visited.add(i)
                    val = cd(i,target,visited.copy(),prod*d[curr][i])
                    if val:
                        res = val
                    visited.remove(i)
            return res
            
            
        for i, j in enumerate(queries):
            if j[inc] not in d or j[out] not in d:
                res.append(-1)
                continue
            val = cd(j[inc],j[out],set(),1)
            res.append(val if val else -1)
        return res
