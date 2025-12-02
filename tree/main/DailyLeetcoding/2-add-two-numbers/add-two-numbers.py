# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        l3 = dummy

        carry = 0

        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if carry > 0:
                carry = 0
            if s > 9:
                s = s % 10
                carry += 1
            
            newNode = ListNode(s)
            dummy.next = newNode
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            dummy.next = ListNode(1)
        
        return l3.next

