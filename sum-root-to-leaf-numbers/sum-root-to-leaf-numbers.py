# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans=0
        def solve(node,aux=0):
            if node==None:
                return
            aux=aux*10+node.val
            if node.left==None and node.right==None:
                self.ans+=aux
            solve(node.left,aux+0)
            solve(node.right,aux+0)
        solve(root)
        return self.ans
        