class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            s = grid[i][j]
            grid[i][j] = 0  
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                s += dfs(x, y) 
            return s
        return max(max(dfs(i, j) for j in range(n)) for i in range(m))
