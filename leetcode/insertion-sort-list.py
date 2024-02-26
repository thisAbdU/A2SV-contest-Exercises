class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(float("-inf"))  # Dummy node to simplify insertion
        dummy.next = head
        prev_sorted = dummy

        while prev_sorted.next:
            curr = prev_sorted.next
            if curr.val >= prev_sorted.val:
                prev_sorted = curr
            else:
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next
                prev_sorted.next = curr.next  # Remove curr from its current position
                curr.next = prev.next
                prev.next = curr

        return dummy.next
