class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid[0])
        m=len(obstacleGrid)
        dp=[[0]*(n+1) for i in range(m+1)]
        for r in range(1,m+1):
            for c in range(1,n+1):
                if r==1 and c==1:
                    if obstacleGrid[r-1][c-1]==1:
                        dp[r][c]=0
                    else:
                        dp[r][c]=1
                elif obstacleGrid[r-1][c-1]==1:
                    dp[r][c]=0
                else:
                    dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[-1][-1]
            