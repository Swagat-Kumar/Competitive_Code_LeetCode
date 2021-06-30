# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDepth(node):
            if node==None:
                return 0
            left=maxDepth(node.left)
            if left==-1:
                return -1
            right=maxDepth(node.right)
            if right==-1 or abs(right-left)>1:
                return -1
            return max(left,right)+1
        return maxDepth(root) != -1