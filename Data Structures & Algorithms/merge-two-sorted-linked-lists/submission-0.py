# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        newHead, current1, current2 = dummyNode, list1, list2
        while current1 and current2:
            if current1.val <= current2.val:
                newHead.next = current1
                current1 = current1.next
            else:
                newHead.next = current2
                current2 = current2.next
            newHead = newHead.next

        if current1:
            newHead.next = current1
        
        if current2:
            newHead.next = current2
        
        return dummyNode.next