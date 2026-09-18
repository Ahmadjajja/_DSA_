class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return

        # Find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split and reverse second half
        second = slow.next
        slow.next = None          # cut here
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge the two halves
        first, second = head, prev
        while second:
            n1, n2 = first.next, second.next
            first.next = second
            second.next = n1
            first, second = n1, n2