# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pS,pE,iS,iE):
            if pE-pS<=0:
                return None
            for i in range(iS,iE):
                if preorder[pS]==inorder[i]:
                    return TreeNode(preorder[pS],build(pS+1,pS+i-iS+1,iS,i),build(pS+i-iS+1,pE,i+1,iE))
        return build(0,len(preorder),0,len(inorder))