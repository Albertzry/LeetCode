class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        flag = [[False for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    dp[i][j] += 1
                    flag[i][j] = True
                elif grid[i][j] == 'Y':
                    dp[i][j] -= 1
                dp[i][j] += dp[i-1][j] if i-1>=0 else 0
                flag[i][j] = True if i-1>=0 and flag[i-1][j] == True else flag[i][j]
                dp[i][j] += dp[i][j-1] if j-1>=0 else 0
                flag[i][j] = True if j-1>=0 and flag[i][j-1] == True else flag[i][j]
                dp[i][j] -= dp[i-1][j-1] if i-1>=0 and j-1>=0 else 0
                flag[i][j] = True if i-1>=0 and j-1>=0 and flag[i-1][j-1] == True else flag[i][j]
                if dp[i][j] == 0 and flag[i][j]:
                    ans+=1
        return ans