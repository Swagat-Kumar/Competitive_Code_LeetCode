"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copied={}
        ans=None
        def clone(node):
            if node==None:
                return None
            if node.val in copied:
                return copied[node.val]
            copy=Node(node.val)
            copied[node.val]=copy
            neighbors=[]
            for n in node.neighbors:
                neighbors.append(clone(n))
            copy.neighbors=neighbors
            return copy
        return clone(node)