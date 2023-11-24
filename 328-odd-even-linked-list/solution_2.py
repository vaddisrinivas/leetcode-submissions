# https://leetcode.com/problems/odd-even-linked-list
# https://leetcode.com/problems/328-odd-even-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            odd, even, evenhead = head, head.next, head.next
        except:
            return head
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next=odd.next
            even = even.next
        odd.next = evenhead
        return head