# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root,left=-2**31-1,right=2**31):
            if root==None:
                return True
            x=root.val
            if left<x and x<right:
                return valid(root.left,left,x) and valid(root.right,x,right)
            return False
        return valid(root)
            