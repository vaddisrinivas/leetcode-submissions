# https://leetcode.com/problems/rotate-array
# https://leetcode.com/problems/189-rotate-array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n #optimization based on fact -> n times rotation == NO rotation

        # reversing the first part of array 
        for i in range((n-k)//2):
            nums[i], nums[n-k-1-i] = nums[n-k-1-i], nums[i]

        # reversing the second part of array
        for i in range(k//2):
            nums[n-k+i], nums[n-1-i] = nums[n-1-i], nums[n-k+i]

        # reversing the entire array
        for i in range(n//2):
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
