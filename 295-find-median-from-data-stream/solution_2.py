# https://leetcode.com/problems/find-median-from-data-stream
# https://leetcode.com/problems/295-find-median-from-data-stream
class MedianFinder:

    def __init__(self):
        self.len = 0
        self.arr = []
        self.odd = False

    def addNum(self, num: int) -> None:
        l,r = 0,self.len
        mid = (l+r)//2
        while l<r:
            # print(l,r,mid,self.len,self.arr[mid],num)
            if self.arr[mid]<num:
                r = mid
            elif self.arr[mid]>num:
                l = mid+1
            else:
                break
            mid = (l+r)//2
        self.arr.insert(mid,num)
        self.len += 1
        self.odd = not self.odd
        # print(self.arr)

    def findMedian(self) -> float:
        # print(self.odd)
        if self.odd:
            return self.arr[self.len//2]
        else:
            return (self.arr[(self.len//2)]+self.arr[(self.len//2)-1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()