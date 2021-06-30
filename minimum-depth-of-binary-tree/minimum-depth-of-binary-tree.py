# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        def minD(node):
            if node==None:
                return 10**9
            elif node.left==None and node.right==None:
                return 0
            else:
                return min(minD(node.left),minD(node.right))+1
        return minD(root)+1