# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(pS,pE,iS,iE):
            if pE-pS<=0:
                return None
            for i in range(iS,iE):
                if postorder[pE-1]==inorder[i]:
                    return TreeNode(postorder[pE-1],build(pS,pS+i-iS,iS,i),build(pS+i-iS,pE-1,i+1,iE))
        return build(0,len(postorder),0,len(inorder))