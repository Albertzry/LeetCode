#bfs
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
#dfs
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or grid[i][j]!="1":
                return
            grid[i][j]="0"
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        result=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    result+=1
        return result
        
