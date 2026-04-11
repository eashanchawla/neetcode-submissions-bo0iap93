# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node, current_node = None, head

        while current_node:
            new_next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = new_next
        return previous_node