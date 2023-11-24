# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# https://leetcode.com/problems/2216-delete-the-middle-node-of-a-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast, prev = head, head, None
        while fast.next:
            prev = slow
            slow = slow.next  
            fast = fast.next.next if fast.next.next else fast.next
        if prev:
            prev.next = slow.next 
            return head
        else:
            return None