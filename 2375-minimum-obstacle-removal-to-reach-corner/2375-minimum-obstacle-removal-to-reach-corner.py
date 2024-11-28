class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m,n=len(grid),len(grid[0])
        q = deque()
        q.append([0,0])
        dis=[[float('inf')]*n for _ in range(m)]
        dis[0][0]=0
        while q:
            i,j=q.popleft()
            for x,y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                if 0<=x<m and 0<=y<n:
                    g=grid[x][y]
                    if dis[i][j]+g<dis[x][y]:
                        dis[x][y]=dis[i][j]+g
                        if g==0:
                            q.appendleft([x,y])
                        else:
                            q.append([x,y])
        return dis[-1][-1]

            