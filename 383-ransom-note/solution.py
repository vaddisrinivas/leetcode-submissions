class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r,s = Counter(ransomNote),Counter(magazine)
        for i in r:
            if not (i in s)  or (s[i]<r[i]):
                return False
        return True