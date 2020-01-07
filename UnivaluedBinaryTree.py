# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.vars = set()
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.vars.add(root.val)
        if root.left:
            self.isUnivalTree(root.left)
        if root.right:
            self.isUnivalTree(root.right)
        if len(self.vars) > 1:
            return False
        else:
            return True
