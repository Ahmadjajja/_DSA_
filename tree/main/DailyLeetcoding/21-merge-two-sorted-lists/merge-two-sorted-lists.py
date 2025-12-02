# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        list3 = dummy

        # list3 : None -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 8
        # None
        # 4 -> 5 -> 8

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            else:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
        
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        return list3.next

# tc : O(n + m)
# sc : O(1)




        
        

