# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self, root: Optional[TreeNode]) -> None:
        temp = root.left
        root.left = root.right
        root.right = temp
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None :
            return None
        self.swap(root)
        if root.left is not None:
            self.invertTree(root.left)
        if root.right is not None:
            self.invertTree(root.right)
        return root