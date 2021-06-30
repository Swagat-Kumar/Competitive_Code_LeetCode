# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.aux=head
        def generate(count):
            if count==0:
                return None
            node=TreeNode()
            node.left=generate(count//2)
            node.val=self.aux.val
            self.aux=self.aux.next
            node.right=generate(count-1-count//2)
            return node
        p=head
        count=0
        while p!=None:
            p=p.next
            count+=1
        return generate(count)