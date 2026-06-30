# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        point1 = list1
        point2 = list2
        temp = out = ListNode()

        while point1 and point2:
            # make out point to point1
            if point1.val <= point2.val:
                out.next = point1
                point1 = point1.next

            # make out point to point2
            else:
                out.next = point2
                point2 = point2.next

            out = out.next
        # point out to whichever list still has values
        if point1:
            out.next = point1
        else:
            out.next = point2
            
        
        return temp.next