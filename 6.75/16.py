class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_ptr= head
        slow_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                slow_ptr = head
                while (slow_ptr != fast_ptr):
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next
                return fast_ptr
        return None