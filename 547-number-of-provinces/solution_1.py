# https://leetcode.com/problems/number-of-provinces
# https://leetcode.com/problems/547-number-of-provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected = []
        for i in range(len(isConnected)):
            # print(isConnected[i])
            temp = [g for g in connected if i+1 in g]
            exists = True if len(temp)>0 else False
            if exists and len(temp)>1:
                for k in temp:
                    connected.remove(k)
                temp = [set().union(*temp)]
                # print(temp,"<---")
                connected.append(temp[0])
            ic = temp[0] if exists else set()
            ic.add(i+1)
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    ic.add(j+1)
            if not exists:
                connected.append(ic)
        
        return len(connected)
# 1,4
# 2,3
# 2,3,4
# 1,3,4