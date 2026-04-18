# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root):
            if not root:
                return True, float('inf'), float('-inf')
            
            lb, lb_min, lb_max = isValid(root.left)
            rb, rb_min, rb_max = isValid(root.right)

            if lb and rb and root.val > lb_max and root.val < rb_min:
                new_min = min(root.val, lb_min)
                new_max = max(root.val, rb_max)
                return True, new_min, new_max
            return False, 0, 0
        
        return isValid(root)[0]
            