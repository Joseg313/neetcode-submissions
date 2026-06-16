# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        
        out = None
        left = head
        right = head.next

        while right:
            left.next = out
            out = left
            left = right
            right = right.next
        
        left.next = out 
        out = left

        return out