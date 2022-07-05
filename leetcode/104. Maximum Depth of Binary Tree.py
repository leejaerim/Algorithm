# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left + 1 if left > right else right + 1 
#after resolving , i realized that was DFS.


#Using BFS
def maxDepth(self, root: TreeNode) -> int:
    
    if not root: return 0
    
    queue = [(root, 1)]
    self.res = 0
    
    while queue:
        root, nums = queue.pop(0)
        
        if not root.left and not root.right:
            self.res = max(self.res, nums)
            
        if root.left:
            queue.append((root.left, nums + 1))
            
        if root.right:
            queue.append((root.right, nums + 1))
            
    return self.res