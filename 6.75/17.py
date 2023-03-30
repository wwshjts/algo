class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr, prev = head, None
        for _ in range(left - 1):
            prev = curr
            curr =curr.next
        new_head = prev
        new_tail = curr
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        new_tail.next = curr

        if new_head:
            new_head.next = prev
        else:
            head = prev
        return head
