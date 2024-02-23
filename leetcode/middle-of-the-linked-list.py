# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size_of_linked_list = 0
        dummy_Node = ListNode(next=head)
        current = dummy_Node.next
        while current:
            current = current.next
            size_of_linked_list += 1
        
        size_of_linked_list //= 2
        middle = dummy_Node.next
        
        for _ in range(size_of_linked_list):
            middle = middle.next
        
        return middle
        
        
