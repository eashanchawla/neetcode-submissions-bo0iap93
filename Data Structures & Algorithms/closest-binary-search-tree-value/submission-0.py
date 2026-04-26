# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff, min_node = float('inf'), float('inf')

        def dfs(root):
            nonlocal min_diff, min_node
            if not root:
                return

            curr_diff = abs(root.val - target)
            if curr_diff < min_diff:
                min_diff = curr_diff
                min_node = root.val
            
            if target > root.val:
                return dfs(root.right)
            else:
                return dfs(root.left)
        dfs(root)
        return min_node
