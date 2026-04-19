# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        mid = self.findMiddle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        while l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True


