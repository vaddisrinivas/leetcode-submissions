# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# https://leetcode.com/problems/19-remove-nth-node-from-end-of-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pprint import pprint
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        l = 1
        oh = head
        prev, next_node = head, head.next
        if prev.next is None and i<n:
            return None
        
        while prev.next is not None:
            l += 1
            prev = prev.next
    
        prev, next_node = head, head.next
        target = l - n -1
        if target == -1:
            return head.next
    
        while prev.next and next_node.next and i<target:
            # print("*****************")
            # pprint(locals())
            prev, next_node =  next_node, next_node.next
            i += 1
        #     pprint(locals())
        # print("*****************")
        # pprint(prev)
    
        prev.next = next_node.next
        return oh