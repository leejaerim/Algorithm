# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is not None and q is not None:
            if self.isSameTree(p.left,q.left) :
                if p.val != q.val :
                    return False
            else:
                return False
            if self.isSameTree(p.right,q.right) :
                if p.val != q.val :
                    return False
            else:
                return False
            return True
        elif p is None and q is None:
            return True
        else:
            return False
    
        