class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        m, n = len(grid), len(grid[0])
        result =0
        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = "0"
            while q:
                x, y = q.popleft()
                for temp_x, temp_y in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
                    if 0 <= temp_x < m and 0 <= temp_y < n and grid[temp_x][temp_y] == "1":
                        q.append((temp_x, temp_y))
                        grid[temp_x][temp_y] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    result+=1
        return result