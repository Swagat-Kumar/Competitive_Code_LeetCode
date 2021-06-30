# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def generate(low,high):
            if low>high:
                return None
            mid=(low+high)//2
            return TreeNode(nums[mid],generate(low,mid-1),generate(mid+1,high))
        return generate(0,len(nums)-1)