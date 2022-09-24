class Solution:
    res = 0
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        else:
            right = self.getHeight(root.right)
            left = self.getHeight(root.left)
            if self.res < (right + left) :
                self.res = right + left
            return max(right,left)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root)
        return self.res