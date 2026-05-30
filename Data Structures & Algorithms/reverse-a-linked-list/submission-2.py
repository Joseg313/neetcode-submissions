# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # if head is empty or linked list has one node just return it
        if head is None or head.next is None:
            return head
        
        
        #initilize 3 pointers
        # out will be returned and contains the current running list of reveresed nodes
        # current keeps track of the current node being reversed
        # forward keeps track of the remaing nodes to be reversed
        out = None
        current = head
        forward = head.next
        
        # stop reversing linked list once forward is empty
        while forward is not None:
            # the current node being reversed should point into the nodes already reversed
            current.next = out
            # set the front of out to now contain the node we just pointed into it
            out = current
            # move on from the node we just reversed
            current = forward
            # break off the node we just reversed from the list of nodes that need to be reversed
            forward = forward.next
            
        
        # reverse the final node
        current.next = out
        out = current
        
        return out

        