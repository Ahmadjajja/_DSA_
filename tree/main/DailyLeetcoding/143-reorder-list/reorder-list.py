# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find starting point of 2nd half

        dummy = ListNode()
        dummy.next = head
        slow = fast = head
        while fast and fast.next:
            dummy = dummy.next
            if slow:
                slow = slow.next
            if fast.next:
                fast = fast.next.next
        if fast:
            slow = slow.next
            dummy = dummy.next
        dummy.next = None

        # reverse 2nd half
        prev = None
        cur = slow

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # re-order the list according to the rules
        start1 = head
        start2 = prev

        while start1 and start2:
            next1 = start1.next
            next2 = start2.next
            start1.next = start2
            start2.next = next1
            start1 = next1
            start2 = next2





        


        