# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if there is no subtree to create
        if not preorder or not inorder:
            return
        
        rootNode = TreeNode(val=preorder[0])
        inorder_index = inorder.index(rootNode.val)
        rootNode.left = self.buildTree(preorder[1: inorder_index + 1], inorder[:inorder_index])
        rootNode.right = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])
        return rootNode