class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(low,high):
            lt=low
            for j in range(low,high):
                if nums[j]>=nums[high]:
                    nums[lt],nums[j]=nums[j],nums[lt]
                    lt+=1
            nums[lt],nums[high]=nums[high],nums[lt]
            return lt
        low=0
        high=len(nums)-1
        while low<=high:
            p=partition(low,high)
            if p==k-1:
                return nums[p]
            elif p>k-1:
                high=p-1
            else:
                low=p+1
        
            