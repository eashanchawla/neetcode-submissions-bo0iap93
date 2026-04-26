# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root.left and not root.right:
            return root.val
        min_diff, min_node = float('inf'), float('inf')
        curr = root

        while curr:
            curr_diff = abs(curr.val - target)
            if curr_diff < min_diff:
                min_diff, min_node = curr_diff, curr.val
            elif curr_diff == min_diff:
                min_node = min(curr.val, min_node)

            if target > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return min_node