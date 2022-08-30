"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None :
            return []
        res.append(root.val)
        for i in root.children:
            res = res + self.preorder(i)
        return res