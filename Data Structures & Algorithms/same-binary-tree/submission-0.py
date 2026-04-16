# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([p]), deque([q])
        
        while q1 and q2:
            curr1 = q1.popleft()
            curr2 = q2.popleft()

            # if both are none
            if not curr1 and not curr2:
                continue
            # if one of them is none
            if not curr1 or not curr2:
                return False
            
            if curr1.val != curr2.val:
                return False
            
            q1.append(curr1.left)
            q1.append(curr1.right)

            q2.append(curr2.left)
            q2.append(curr2.right)

        return True
