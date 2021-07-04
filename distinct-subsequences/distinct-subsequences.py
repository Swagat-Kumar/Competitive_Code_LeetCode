import numpy as np
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[0]*(len(s)+1) for i in range(len(t)+1)]
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                if r==0 and c==0:
                    dp[r][c]=1
                elif r==0:
                    dp[r][c]=1
                elif c==0:
                    dp[r][c]=0
                elif s[c-1]==t[r-1]:
                    dp[r][c]=dp[r-1][c-1]+dp[r][c-1]
                else:
                    dp[r][c]=dp[r][c-1]
        return dp[-1][-1]