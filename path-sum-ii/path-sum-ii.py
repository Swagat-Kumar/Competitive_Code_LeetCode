# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans=[]
        if root==None:
            return ans
        def solve(node,aux=[],summ=0):
            if node==None:
                return
            if node.left==None and node.right==None:
                if summ+node.val==targetSum:
                    copy=list(aux)
                    copy.append(node.val)
                    ans.append(copy)
                return
            copy=list(aux)
            copy.append(node.val)
            solve(node.left,copy,summ+node.val)
            copy=list(aux)
            copy.append(node.val)
            solve(node.right,copy,summ+node.val)
        solve(root)
        return ans