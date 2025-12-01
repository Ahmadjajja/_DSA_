# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev

        # def reverse(cur, prev):
        #     if not cur:
        #         return prev

        #     next = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next

        #     return reverse(cur, prev)
        
        # return reverse(head, None)


