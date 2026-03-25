class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] += grid[i][j]
                dp[i][j] += dp[i-1][j] if i-1>=0 else 0
                dp[i][j] += dp[i][j-1] if j-1>=0 else 0
                dp[i][j] -= dp[i-1][j-1] if i-1>=0 and j-1>=0 else 0
        
        for i in range(m-1):
            if dp[i][n-1] == dp[m-1][n-1] - dp[i][n-1]:
                return True
        
        for j in range(n-1):
            if dp[m-1][j] == dp[m-1][n-1] - dp[m-1][j]:
                return True
        
        return False