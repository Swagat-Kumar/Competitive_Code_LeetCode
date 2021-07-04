# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        aux=[root]
        while len(aux)!=0:
            node=aux.pop()
            if node.right!=None:
                aux.append(node.right)
            if node.left!=None:
                aux.append(node.left)
            if len(aux)!=0:
                node.right=aux[-1]
            node.left=None
            