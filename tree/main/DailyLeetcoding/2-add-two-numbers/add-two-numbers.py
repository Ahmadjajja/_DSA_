# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, None)
        l3 = dummy

        carry = 0
        while l1 or l2 or carry:
            curSum = carry
            if l1:
                curSum += l1.val
                l1 = l1.next
            if l2:
                curSum += l2.val
                l2 = l2.next
            
            carry = curSum // 10
            l3.next = ListNode(curSum % 10, None)
            l3 = l3.next
        
        return dummy.next