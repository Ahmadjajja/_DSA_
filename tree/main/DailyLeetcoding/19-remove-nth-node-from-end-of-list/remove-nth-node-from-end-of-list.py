# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # count total elements in one pass -> 1st pass
        countNodes = 0
        dummy = ListNode(None)
        prev = dummy
        prev.next = head
        cur = head
        while cur:
            countNodes += 1
            cur = cur.next
        
        # correct_pos = 5 - 2 + 1 = 4
        pos = countNodes - n + 1
        
        # we will go by 2nd pass and remove at that location -> 2nd pass
        curPos = 0
        cur = head
        while cur:
            curPos += 1
            if pos == curPos:
                prev.next = cur.next
                break
            prev = prev.next
            cur = cur.next
        
        return dummy.next
        
        