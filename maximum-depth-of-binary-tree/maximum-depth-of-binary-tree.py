# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max=0
        def travel(root,level=0):
            if root==None:
                return
            self.max=max(self.max,level+1)
            travel(root.left,level+1)
            travel(root.right,level+1)
        travel(root)
        return self.max