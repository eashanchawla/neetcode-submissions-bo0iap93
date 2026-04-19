# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numList = [] 
        curr = head
        while curr:
            numList.append(curr.val)
            curr = curr.next
        return numList == list(reversed(numList))