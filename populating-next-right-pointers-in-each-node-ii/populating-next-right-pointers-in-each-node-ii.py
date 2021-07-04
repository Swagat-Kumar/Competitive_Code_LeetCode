"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return None
        aux=[root]
        while len(aux)!=0:
            for i in range(len(aux)-1):
                aux[i].next=aux[i+1]
            aux[-1].next=None
            temp=[]
            for a in aux:
                if a.left:
                    temp.append(a.left)
                if a.right:
                    temp.append(a.right)
            aux=temp
        return root