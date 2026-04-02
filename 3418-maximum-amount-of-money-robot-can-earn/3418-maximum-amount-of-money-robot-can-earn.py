class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-inf] * 3 for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = coins[0][0]
        for k in range(1, 3):
            dp[0][0][k] = max(coins[0][0], 0)
        
        for j in range(1, n):
            dp[0][j][0] = dp[0][j-1][0] + coins[0][j]
            x = max(coins[0][j], 0)
            for k in range(1, 3):
                dp[0][j][k] = max(dp[0][j - 1][k] + coins[0][j], dp[0][j - 1][k - 1] + x)
        
        for i in range(1, m):
            dp[i][0][0] = dp[i - 1][0][0] + coins[i][0]
            x = max(coins[i][0], 0)
            for k in range(1, 3):
                dp[i][0][k] = max(dp[i - 1][0][k] + coins[i][0], dp[i - 1][0][k - 1] + x) 
        
        for i in range(1, m):
            for j in range(1, n):
                x = coins[i][j]
                dp[i][j][2] = max(dp[i - 1][j][2] + x, dp[i][j - 1][2] + x, dp[i - 1][j][1], dp[i][j - 1][1])
                dp[i][j][1] = max(dp[i - 1][j][1] + x, dp[i][j - 1][1] + x, dp[i - 1][j][0], dp[i][j - 1][0])
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0]) + x
        
        return dp[m - 1][n - 1][2]
