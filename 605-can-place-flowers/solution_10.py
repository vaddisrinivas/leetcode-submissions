# https://leetcode.com/problems/can-place-flowers
# https://leetcode.com/problems/605-can-place-flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while n>0 and i< len(flowerbed):
            if flowerbed[i]==0 and flowerbed[max(0,i-1)]==0 and flowerbed[min(i+1,len(flowerbed)-1)]==0:
                flowerbed[i]=1    
                n-=1
            i += 1
        return n==0


        