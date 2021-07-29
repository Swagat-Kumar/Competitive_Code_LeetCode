# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p=[]
        self.prev=None
        self.first=None
        self.second=None
        def solve(node=root):
            if node==None:
                return
            solve(node.left)
            if self.prev!=None and self.prev.val>node.val and self.first==None:
                self.first=self.prev
            if self.prev!=None and self.first!=None and self.prev.val>node.val:
                self.second=node
            self.prev=node
            solve(node.right)
        solve()
        a=self.first
        b=self.second
        a.val,b.val=b.val,a.val