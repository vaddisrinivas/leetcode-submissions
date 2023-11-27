# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p,q = l1,l2
        carry = 0
        while l1 and l2:
            s = l1.val+l2.val+carry
            if s>9:
                l1.val = int(str(s)[1])
                carry = int(str(s)[0])
            else:
                l1.val = s
                carry = 0
            if l1.next==None and l2.next is not None:
                l1.next, l2.next = l2.next, None
            elif l1.next is None and l2.next is None:
                if carry: l1.next = ListNode(carry)
                carry = 0
            l1, l2 = l1.next, l2.next 
        
        while carry and l1:
            # print(carry,l1.val)
            s = l1.val+carry
            if s>9:
                l1.val = int(str(s)[1])
                carry = int(str(s)[0])
            else:
                l1.val = s
                carry = 0
            if carry and l1.next is None:
                l1.next = ListNode(carry)
                break
            l1 = l1.next
        return p