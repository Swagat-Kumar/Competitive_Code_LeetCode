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
        aux=[]
        temp=[]
        def solve(node=root):
            if node==None:
                return
            solve(node.left)
            aux.append(node.val)
            temp.append(node)
            solve(node.right)
        solve()
        p=[]
        sorted_aux=sorted(aux)
        for i in range(len(aux)):
            if sorted_aux[i]!=aux[i]:
                p.append(i)
        a=temp[p[0]]
        b=temp[p[1]]
        a.val,b.val=b.val,a.val
        
        