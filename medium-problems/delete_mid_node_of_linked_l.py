class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        mid_idx = length // 2

        current = head
        for _ in range(mid_idx - 1):
            current = current.next

        current.next = current.next.next

        return head

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        if not head.next.next:
            head.next = None
            return head

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head