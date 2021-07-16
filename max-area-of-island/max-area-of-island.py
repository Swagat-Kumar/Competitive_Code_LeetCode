class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=[[False]*len(grid[0]) for i in range(len(grid))]
        count=0
        self.v=0
        def dfs(r,c):
            if r<0 or c<0 or c>=len(grid[0]) or r>=len(grid):
                return
            if visited[r][c]:
                return
            if grid[r][c]==1:
                self.v+=1
                visited[r][c]=True
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visited[r][c] and grid[r][c]==1:
                    dfs(r,c)
                    count=max(count,self.v)
                    self.v=0
        return count