# https://leetcode.com/problems/successful-pairs-of-spells-and-potions
# https://leetcode.com/problems/2392-successful-pairs-of-spells-and-potions
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        l = len(potions)
        def bns(target):
            m = l//2
            x, y = 0, l
            while x<y:
                if potions[m] >= target:
                    y = m
                elif potions[m] < target:
                    x = m+1
                else:
                    break
                m = (x+y)//2
            return m
        return  [l-bns(success/i) for i in spells]