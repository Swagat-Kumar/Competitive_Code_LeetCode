# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1,t2):
            if t1==None and t2==None:
                return True
            if t1==None or t2==None:
                return False
            if t1.val!=t2.val:
                return False
            return isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)
        t1=root
        t2=root
        return isMirror(t1,t2)