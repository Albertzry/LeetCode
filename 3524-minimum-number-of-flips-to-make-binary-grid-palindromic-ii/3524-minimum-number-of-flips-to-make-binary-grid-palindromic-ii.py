class Solution(object):
    def minFlips(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m // 2):
            for j in range(n // 2):
                cnt1 = grid[i][j] + grid[i][n - 1 - j] + \
                       grid[m - 1 - i][j] + grid[m - 1 - i][n - 1 - j]
                ans += min(cnt1, 4 - cnt1)

        diff, cnt1 = 0, 0
        if m % 2 == 1:
            for j in range(n // 2):
                if grid[m // 2][j] ^ grid[m // 2][n - 1 - j]:
                    diff += 1
                else:
                    cnt1 += grid[m // 2][j] * 2
        if n % 2 == 1:
            for i in range(m // 2):
                if grid[i][n // 2] ^ grid[m - 1 - i][n // 2]:
                    diff += 1
                else:
                    cnt1 += grid[i][n // 2] * 2
        if m % 2 == 1 and n % 2 == 1:
            ans += grid[m // 2][n // 2]
        if diff > 0:
            ans += diff
        else:
            ans += cnt1 % 4
        return ans