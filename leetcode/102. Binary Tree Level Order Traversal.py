class Solution:
    res = []
    def levelOrderTraversal(self,root:Optional[TreeNode], depth : int ) -> None:
        if root is None : 
            return
        if len(self.res) <= depth:
            self.res.append([root.val])
        else:
            self.res[depth].append(root.val)
        self.levelOrderTraversal(root.left,depth+1)
        self.levelOrderTraversal(root.right,depth+1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.levelOrderTraversal(root,0)
        return self.res