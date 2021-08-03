class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False]*(len(s2)+1) for i in range(len(s1)+1)]
        for r in range(len(s1)+1):
            for c in range(len(s2)+1):
                if r==0 and c==0:
                    dp[r][c]=True
                elif r==0:
                    if s2[c-1]==s3[c-1]:
                        dp[r][c]=dp[r][c-1]
                elif c==0:
                    if s1[r-1]==s3[r-1]:
                        dp[r][c]=dp[r-1][c]
                else:
                    dp[r][c]=s3[r+c-1]==s2[c-1] and dp[r][c-1]
                    dp[r][c]=dp[r][c] or (s3[r+c-1]==s1[r-1] and dp[r-1][c])
        return dp[-1][-1]