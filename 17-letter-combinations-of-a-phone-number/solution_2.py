# https://leetcode.com/problems/letter-combinations-of-a-phone-number
# https://leetcode.com/problems/17-letter-combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        l = len(digits)
        if l==0:
            return []
        # tail recursion
        def bt(curr_str,curr_digit,res):
            if len(curr_str)==l-1:
                for i in d[digits[curr_digit]]:
                    res += [curr_str+i]
                return res
            else:
                for i in d[digits[curr_digit]]:
                    res = bt(curr_str+i,curr_digit+1,res)
                return res
        return bt("",0,[])
        # 233