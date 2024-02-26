# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = ListNode()
        not_smaller_head = ListNode()

        smaller_curr = smaller_head
        not_smaller_curr = not_smaller_head

        while head:
            if head.val < x:
                smaller_curr.next = head
                smaller_curr = smaller_curr.next
            else:
                not_smaller_curr.next = head
                not_smaller_curr = not_smaller_curr.next
            head = head.next
        
        smaller_curr.next = not_smaller_head.next
        not_smaller_curr.next = None

        return smaller_head.next