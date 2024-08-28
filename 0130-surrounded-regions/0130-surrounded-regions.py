class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or board[i][j]!="O":
                return
            board[i][j]="Z"
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="Z":
                    board[i][j]="O"
        return board
        

            