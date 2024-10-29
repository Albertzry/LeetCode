class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i: int, j: int) -> None:
            nonlocal ans
            ans = max(ans, j)
            if ans == n - 1:  # ans 已达到最大值
                return
            for k in i - 1, i, i + 1:  # 向右上/右/右下走一步
                if 0 <= k < m and grid[k][j + 1] > grid[i][j]:
                    dfs(k, j + 1)
            grid[i][j] = 0
        for i in range(m):
            dfs(i, 0)  # 从第一列的任一单元格出发
        return ans
