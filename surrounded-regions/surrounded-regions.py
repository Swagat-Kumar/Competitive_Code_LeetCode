class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited=[[False]*len(board[0]) for i in range(len(board))]
        def dfs(x,y):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
                return
            if visited[x][y]:
                return
            if board[x][y]=='O':
                board[x][y]='1'
                visited[x][y]=True
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
        for i in range(len(board[0])):
            if board[0][i]=='O':
                dfs(0,i)
        for i in range(len(board[0])):
            if board[-1][i]=='O':
                dfs(len(board)-1,i)
        for i in range(1,len(board)-1):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][len(board[0])-1]=='O':
                dfs(i,len(board[0])-1)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='X':
                    continue
                if board[r][c]=='1':
                    board[r][c]='O'
                else:
                    board[r][c]='X'