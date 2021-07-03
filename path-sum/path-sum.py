# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root==None:
            return False
        self.ans=False
        def solve(root,summ):
            if root==None:
                return
            if (root.left==None and root.right==None) or self.ans:
                if summ+root.val==targetSum:
                    self.ans=True
                return
            solve(root.left,summ+root.val)
            solve(root.right,summ+root.val)
        solve(root,0)
        return self.ans
            