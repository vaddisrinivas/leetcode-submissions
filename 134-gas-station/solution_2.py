# https://leetcode.com/problems/gas-station
# https://leetcode.com/problems/134-gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = list(accumulate([gas[i]-cost[i] for i in range(len(gas))]))
        if diffs[-1]<0:return -1
        m,ind = diffs[0],0
        for i in range(1,len(diffs)):
            if diffs[i]<=m:
                m,ind = diffs[i],i
        return (ind+1)%len(gas)
