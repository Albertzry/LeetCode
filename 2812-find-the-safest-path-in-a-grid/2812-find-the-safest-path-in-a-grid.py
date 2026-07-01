class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
        
        dis = [[-1] * n for _ in range(n)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dis[i][j] = 0
        
        while q:
            cx, cy = q.popleft()
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == -1:
                    dis[nx][ny] = dis[cx][cy] + 1
                    q.append((nx, ny))
        
        def check(limit: int) -> bool:
            visit = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visit[0][0] = True
            
            while q:
                cx, cy = q.popleft()
                if cx == n - 1 and cy == n - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if (0 <= nx < n and 0 <= ny < n and 
                        not visit[nx][ny] and dis[nx][ny] >= limit):
                        q.append((nx, ny))
                        visit[nx][ny] = True
            return False
        
        lo, hi = 0, min(dis[0][0], dis[n - 1][n - 1])
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
