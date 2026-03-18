class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        mt = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                mt[i][j] += grid[i][j]
                mt[i][j] += mt[i-1][j] if i-1 >= 0 else 0
                mt[i][j] += mt[i][j-1] if j-1 >= 0 else 0
                mt[i][j] -= mt[i-1][j-1] if i-1>=0 and j-1 >=0 else 0
                ans += 1 if mt[i][j] <= k else 0
        
        return ans
        