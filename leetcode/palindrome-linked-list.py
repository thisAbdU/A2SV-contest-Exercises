# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
        
        first = head
        second = pre
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
        