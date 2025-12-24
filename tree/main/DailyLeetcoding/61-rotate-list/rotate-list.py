class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. Get length
        length = 0
        tail = head
        while tail:
            tail = tail.next
            length += 1

        # 2. Normalize k
        k %= length
        if k == 0:
            return head

        # 3. Two pointers
        slow = fast = head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # 4. Rotate
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head
