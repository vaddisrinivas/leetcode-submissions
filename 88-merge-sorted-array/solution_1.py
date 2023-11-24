# https://leetcode.com/problems/merge-sorted-array
# https://leetcode.com/problems/88-merge-sorted-array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        k = len(nums1)-1
        while i>-1 and j >-1:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            elif nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            else:
                nums1[k]=nums1[i]
                k-=1
                nums1[k]=nums2[j]
                j-=1
                i-=1
                k-=1
        # print(nums1,nums2,i,j,k)
        if j>-1:
            for z in range(j,-1,-1):
                nums1[z]=nums2[j]
                j -= 1
        return
            
            