# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        tempA, tempB = headA, headB
        while tempA:
            tempA = tempA.next
            lenA += 1
        
        while tempB:
            tempB = tempB.next
            lenB += 1
        
        if tempA != tempB:
            return None

        offset = lenA - lenB
     
        if offset > 0:
            while offset > 0:
                headA = headA.next
                offset -= 1
        else:
            offset = abs(offset)
    
            while offset > 0:
                headB = headB.next
                offset -= 1

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return 

        