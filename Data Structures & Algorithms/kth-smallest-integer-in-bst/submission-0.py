# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order_list = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            in_order_list.append(root.val)
            dfs(root.right)
        
        dfs(root)
        # if len(in_order_list) >= k:
        return in_order_list[k - 1]

