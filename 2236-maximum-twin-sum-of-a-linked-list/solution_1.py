# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
# https://leetcode.com/problems/2236-maximum-twin-sum-of-a-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        arr = []
        m = 0
        c = 0
        while slow is not None:
            c += 1
            slow = slow.next
        t = 0
        slow = head
        while slow is not None:
            if t<c//2:
                arr += [slow.val]
            else:
                m = max(m,arr.pop() +slow.val)
            slow = slow.next
            t += 1
        return m


        