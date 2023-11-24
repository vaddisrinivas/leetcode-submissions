# https://leetcode.com/problems/product-of-array-except-self
# https://leetcode.com/problems/238-product-of-array-except-self
from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1
        i = prod(nums)
        count_zeros = nums.count(0)
        if i==0 and count_zeros == 1:
            product = prod(nums[:nums.index(0)])*prod(nums[nums.index(0)+1:])
            for m,n in enumerate(nums):
                if n==0:
                    nums[m] = product
                else:
                    nums[m] = 0        
        elif i==0 and count_zeros!=1:
            for m,n in enumerate(nums):
               nums[m] = 0
        else:
            for m,n in enumerate(nums):
                nums[m] = i//n
        return nums