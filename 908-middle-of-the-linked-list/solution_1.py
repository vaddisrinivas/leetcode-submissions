# https://leetcode.com/problems/middle-of-the-linked-list
# https://leetcode.com/problems/908-middle-of-the-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = s = head
        while s.next is not None:
            f = f.next
            s = s.next
            if s.next is not None:
                s = s.next
        return f
        
        