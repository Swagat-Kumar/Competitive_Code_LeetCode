# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        def travel(root,level=0):
            if root==None:
                return
            if level==len(ans):
                ans.insert(0,[])
            ans[-1-level].append(root.val)
            travel(root.left,level+1)
            travel(root.right,level+1)
        travel(root)
        return ans
            