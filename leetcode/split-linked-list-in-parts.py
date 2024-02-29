import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        part_size = count // k
        remaining = count % k
        
        output = []
        current = head
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < remaining else 0)
            if part_head:
                for _ in range(part_length - 1):
                    current = current.next
                next_part = current.next
                current.next = None
                output.append(part_head)
                current = next_part
            else:
                output.append(None)
        
        return output
