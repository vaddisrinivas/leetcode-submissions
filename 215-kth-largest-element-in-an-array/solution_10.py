# https://leetcode.com/problems/kth-largest-element-in-an-array
# https://leetcode.com/problems/215-kth-largest-element-in-an-array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(heap):
            m = len(heap)-1
            n =  0
            while n<=(m+1)//2:
                l, r = min(2*n+1,m),min( 2*n+2,m)
                largest = n
                if heap[r]<heap[largest]:
                    largest = r
                if heap[l]<heap[largest]:
                    largest = l
                    if heap[r]<heap[l]:
                        largest = r
                if largest!=n:
                    heap[n],heap[largest] = heap[largest],heap[n]
                    n = largest
                else:
                    break
            return heap

        def heap_up(heap):
            n= len(heap)-1
            while n>0:
                if heap[(n-1)//2]>heap[n]:
                    heap[(n-1)//2], heap[n]=heap[n],heap[(n-1)//2]
                    n = (n-1) //2
                else:
                    break
            return heap   
        heap = []
        for j,i in enumerate(nums):
            if j < k:
                heap.append(i)
                heap = heap_up(heap)
                continue
            if heap[0]<=i:
                heap[0] = i
                heap = heapify(heap)

        return heap[0]