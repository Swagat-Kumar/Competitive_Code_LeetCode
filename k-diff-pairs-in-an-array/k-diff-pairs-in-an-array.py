import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic=collections.defaultdict(int)
        for n in nums:
            dic[n]+=1
        aux=set()
        for n in dic:
            if (k>0 and n+k in dic) or (k==0 and dic[n]>1):
                aux.add(n)
        print(aux)
        return len(aux)
        