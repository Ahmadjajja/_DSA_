# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return
        slow = fast = head

        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split and merge 2nd half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        half1 = head
        half2 = prev

        while half2:
            next1 = half1.next
            next2 = half2.next

            half1.next = half2
            half2.next = next1
            half2 = next2
            half1 = next1
        
        