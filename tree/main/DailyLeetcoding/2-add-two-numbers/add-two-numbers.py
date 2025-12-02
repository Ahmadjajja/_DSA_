# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 243 -> 342
        # 564 -> 465
        # 708 -> 807

        dummy = ListNode(None)
        l3 = dummy

        carry = 0

        while l1 and l2:
            s = l1.val + l2.val + carry
            if carry > 0:
                carry = 0
            if s > 9:
                s = s % 10
                carry += 1
            
            newNode = ListNode(s)
            dummy.next = newNode
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                s = l1.val + carry
                if carry > 0:
                    carry = 0
                if s > 9:
                    s = s % 10
                    carry += 1
                
                newNode = ListNode(s)
                dummy.next = newNode
                dummy = dummy.next
                l1 = l1.next
        if l2:
            while l2:
                s = l2.val + carry
                if carry > 0:
                    carry = 0
                if s > 9:
                    s = s % 10
                    carry += 1
                
                newNode = ListNode(s)
                dummy.next = newNode
                dummy = dummy.next
                l2 = l2.next
        
        if carry > 0:
            dummy.next = ListNode(1)
        
        return l3.next

