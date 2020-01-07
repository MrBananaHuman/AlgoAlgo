"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.output = []
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        for i in root.children:
            self.postorder(i)
            self.output.append(i.val)
        return self.output + [root.val]
        
