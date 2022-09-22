# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = True
    def calcDf(self, root: Optional[TreeNode]) -> int:
        if root is None : 
            return 0
        else:
            left = self.calcDf(root.left)
            right = self.calcDf(root.right)
            if abs(left-right) > 1:
                self.res = False
            return max(left,right)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.calcDf(root)
        return self.res