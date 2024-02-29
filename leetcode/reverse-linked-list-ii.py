class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next

        current = pre.next
        rev_head, rev_tail = None, current

        for _ in range(right - left + 1):
            temp = current.next
            current.next = rev_head
            rev_head = current
            current = temp

        pre.next = rev_head
        rev_tail.next = current

        return dummy.next
