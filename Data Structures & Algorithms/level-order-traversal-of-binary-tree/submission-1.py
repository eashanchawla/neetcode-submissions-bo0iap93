# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_order = []
        queue = deque([root])
        level = 0
        while queue:
            level_l = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_l.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level_order.append(level_l)
        return level_order


