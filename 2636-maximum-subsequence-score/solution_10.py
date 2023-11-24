# https://leetcode.com/problems/maximum-subsequence-score
# https://leetcode.com/problems/2636-maximum-subsequence-score
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # Building a list of tuples to represent pairs
        pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
        
        # Sorting pairs by the corresponding value in nums2
        pairs.sort(key = lambda pair : pair[1], reverse = True)

        minHeap = []
        n1Sum = 0
        result = 0 # max score

        for num1, num2 in pairs:
            n1Sum += num1
            heapq.heappush(minHeap, num1)

            if len(minHeap) > k:
                n1Sum -= heapq.heappop(minHeap)
            
            if len(minHeap) == k:
                result = max(result, n1Sum * num2)

        return result