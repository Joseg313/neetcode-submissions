# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        begin = None
        mid = head
        end = head.next

        while end:
            mid.next = begin
            begin = mid
            mid = end
            end = end.next
        
        mid.next = begin
        begin = mid
        



        return begin

