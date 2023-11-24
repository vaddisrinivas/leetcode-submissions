# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# https://leetcode.com/problems/28-find-the-index-of-the-first-occurrence-in-a-string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        key_dict = {needle[i]:i for i in range(len(needle))}
        print(key_dict)
        ph, pn = len(needle)-1,len(needle)-1
        
        while ph<len(haystack):
            # print(f"haystack {haystack} at {ph} {haystack[ph]} needle {needle} at {pn} {needle[pn]}")
            if haystack[ph] == needle[pn]:
                if pn==0:
                    return ph
                ph -= 1
                pn -= 1
            else:
                if haystack[ph] in key_dict:
                    ph += len(needle) - min(key_dict[haystack[ph]]+1,pn)
                else:
                    ph += len(needle)
                pn = len(needle) -1
        if pn==-1:
            return ph+1
        else:
            return -1