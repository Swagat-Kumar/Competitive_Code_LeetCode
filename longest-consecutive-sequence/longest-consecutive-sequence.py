class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aux={}
        for n in nums:
            aux[n]=True
        nums=list(aux)
        if len(nums)==0:
            return 0
        nums.sort()
        ans=0
        count=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            else:
                ans=max(count,ans)
                count=1
        ans=max(count,ans)
        return ans