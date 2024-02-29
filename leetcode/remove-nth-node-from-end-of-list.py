# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_Node = ListNode(val=0, next=head)
        fast = slow = dummy_Node
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast, slow = fast.next, slow.next
            
        slow.next = slow.next.next
        
        return dummy_Node.next
    
            
        
        
         