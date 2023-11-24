# https://leetcode.com/problems/domino-and-tromino-tiling
# https://leetcode.com/problems/806-domino-and-tromino-tiling
class Solution:
    def numTilings(self, n: int) -> int:
        count = 0
        if n<=2:
            return n
        dp = {}
        def ind(t1,t2):
            if t1 and t2:
                return 0
            if t1 and not t2:
                return 1
            if not t1 and t2:
                return 2
            if not t1 and not t2:
                return 3
        
        def solve(i,t1,t2):
            if i==n:
                return 1
            count = 0
            t3, t4 = i+1<n, i+1<n 
            if i in dp and dp[i][ind(t1,t2)] is not None:
                return dp[i][ind(t1,t2)]
            # t1 and t2 are available; means we can fill t1, t2 or t1,t2,t3 or t1,t2,t4
            if t1 and t2: count+=solve(i+1, True, True) 
            if t1 and t2 and t3 : count+=solve(i+1, True, False) 
            if t1 and t2 and t3 : count+=solve(i+1, False, True)
            if t1 and t2 and t3 : count+=solve(i+1, False, False)
            
            # t1 and t2 are filled - so move to next column
            if not t1 and not t2 : count+=solve(i+1,True, True)
            # t1 is available but t2 is not; means we can fill t1, t3 or t1,t3,t4
            if t1 and not t2 and t3 : count+=solve(i+1,False, True)
            if t1 and not t2 and t3 : count+=solve(i+1, False, False)
            # t1 is not available but t2 is; means we can fill t2, t4 or t2,t3,t4
            if not t1 and t2 and t3 : count+=solve(i+1,True,False)
            if not t1 and t2 and t3 : count+=solve(i+1,False,False)
            if i not in dp:
                dp[i] =[None]*4
            dp[i][ind(t1,t2)] = count
            return count
        
        count = solve(0,True, True)
        # print(dp)
        return count%(10**9+7)
            