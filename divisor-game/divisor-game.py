class Solution:
    def divisorGame(self, n: int) -> bool:
        dp=[False]*(n+1)
        for i in range(2,n+1):
            for x in range(1,i):
                if i%x==0:
                    if not dp[i-x]:
                        dp[i]=True
        return dp[-1]
        