# https://leetcode.com/problems/greatest-common-divisor-of-strings
# https://leetcode.com/problems/1146-greatest-common-divisor-of-strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        i, j = 0,0
        res = ""
        s1, s2 = set(str1),set(str2)
        def makeStr(s, x):
            return s*(x.count(s))==x
        while i< len(str1) and j<len(str2):
            curr1, curr2 = str1[:i+1],str2[:j+1]
            if curr1==curr2:
                if (makeStr(curr1,str1) and makeStr(curr1,str2)):
                  res = curr1
            else:
                return res
            i+=1
            j+=1
        return res
