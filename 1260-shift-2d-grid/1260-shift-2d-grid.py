class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),  len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        p = m-1-floor(k/n)%m
        q = n-k%n
        if q == n:
            q=0
            p+=1
            if p == m:
                p=0
        for i in range(m):
            for j in range(n):
                ans[i][j] = grid[p][q]
                if q == n-1 and p == m-1:
                    p=0
                    q=0
                    continue
                q+=1
                if q == n:
                    q=0
                    p+=1
        return ans