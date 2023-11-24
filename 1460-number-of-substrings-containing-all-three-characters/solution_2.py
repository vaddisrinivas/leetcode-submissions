# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters
# https://leetcode.com/problems/1460-number-of-substrings-containing-all-three-characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = len(s)
        c = 0
        if l < 3:
            return 0
        
        ss = {'a', 'b', 'c'}
        curr_ss = {char: 0 for char in ss}
        start = 0
        ind = 0
        
        while ind < l:
            curr_ss[s[ind]] += 1
            
            while all(curr_ss[char] > 0 for char in ss):
                c += l - ind
                curr_ss[s[start]] -= 1
                start += 1
            
            ind += 1
        
        return c
