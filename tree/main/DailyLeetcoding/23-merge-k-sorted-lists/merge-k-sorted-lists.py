# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        minH = []
        for i, lis in enumerate(lists):
            if lis:
                minH.append((lis.val, i, lis))
        
        heapq.heapify(minH)

        dummy = cur = ListNode()
        while minH:
            val, i, node = heapq.heappop(minH)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(minH, (node.next.val, i, node.next))
        
        return dummy.next