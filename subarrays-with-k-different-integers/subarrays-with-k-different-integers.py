import collections
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            left=0
            aux=0
            dic=collections.defaultdict(int)
            for i,n in enumerate(nums):
                dic[n]+=1
                while len(dic)>k:
                    dic[nums[left]]-=1
                    if dic[nums[left]]==0:
                        del dic[nums[left]]
                    left+=1
                aux+=i-left+1
            return aux
        return atMostK(k)-atMostK(k-1)
    