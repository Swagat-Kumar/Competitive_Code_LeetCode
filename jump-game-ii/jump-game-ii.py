import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=[sys.maxsize]*len(nums)
        jumps[0]=0
        for i in range(len(nums)):
            for x in range(i+1,min(i+nums[i]+1,len(nums))):
                jumps[x]=min(jumps[x],jumps[i]+1)
        return jumps[-1]
                