import collections
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        pre=[collections.Counter()]*(len(s)+1)
        for i in range(1,len(s)+1):
            pre[i]=pre[i-1]+Counter(s[i-1])
        n=len(queries)
        ans=[False for _ in range(n)]
        for i in range(n):
            start,end,k=queries[i]
            dic=pre[end+1]-pre[start]
            odd=0
            for c, cnt in dic.items():
                if cnt%2!=0:
                    odd+=1
            if odd//2<=k:
                ans[i]=True
        return ans