# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def visit(node):
            if node==None:
                return
            ans.append(node.val)
            visit(node.left)
            visit(node.right)
        visit(root)
        return ans