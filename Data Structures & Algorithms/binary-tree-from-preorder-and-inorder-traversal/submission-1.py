# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        root_idx = 0
        def dfs(l, r):
            nonlocal root_idx
            if l > r:
                return None 
            
            root_val = preorder[root_idx]
            root_idx += 1
            mid = indices[root_val]
            rootNode = TreeNode(root_val)
            rootNode.left = dfs(l, mid - 1)
            rootNode.right = dfs(mid + 1, r)
            return rootNode
        return dfs(0, len(inorder) - 1)
        