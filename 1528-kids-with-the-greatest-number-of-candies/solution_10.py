# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# https://leetcode.com/problems/1528-kids-with-the-greatest-number-of-candies
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = max(candies)
        return [True if i+extraCandies>=m else False for i in candies]