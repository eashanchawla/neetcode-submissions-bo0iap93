# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        
    def reverseLinkedList(self, head):
        # base case 
        if not head or not head.next:
            return head
        newHead = self.reverseLinkedList(head.next)

        head.next.next = head
        head.next = None
        return newHead

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        # find middle and reverse second half
        l1 = head
        middle_node = self.findMiddle(head)
        l2 = self.reverseLinkedList(middle_node.next)
        middle_node.next = None
        
        while l2:
            templ1_next = l1.next
            templ2_next = l2.next
            l1.next = l2
            l2.next = templ1_next
            l1 = l2.next
            l2 = templ2_next
        