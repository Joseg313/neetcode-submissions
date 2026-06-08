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
        current = head
        nex = head.next

        while current.next != None:
            current.next = out
            out=current
            current = nex
            nex = nex.next
        current.next = out
        out=current


        return out