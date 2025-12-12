class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) Find middle (slow ends at mid)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Split into two lists: head..mid and second..
        second = slow.next
        slow.next = None

        # 3) Reverse second half
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev  # new head of reversed half

        # 4) Merge: L0 -> R0 -> L1 -> R1 ...
        first = head
        while second:
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2
