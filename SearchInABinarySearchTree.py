# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    tempNode = None
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current_var = root.val
        if val == current_var:
            self.tempNode = root
        else:
            if root.left:
                self.searchBST(root.left, val)
            if root.right:
                self.searchBST(root.right, val)
        return self.tempNode
