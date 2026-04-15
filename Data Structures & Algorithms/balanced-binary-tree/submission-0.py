# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return (True, 0)
            
            lb = dfs(root.left)
            rb = dfs(root.right)

            balanced = lb[0] and rb[0] and abs(lb[1] - rb[1]) <= 1
            return (balanced, 1 + max(lb[1], rb[1]))
        return dfs(root)[0]
