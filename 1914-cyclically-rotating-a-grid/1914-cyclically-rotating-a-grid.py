class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        limit = min(int(m / 2), int(n / 2))
        for i in range(limit):
            x1, x2 = i, m - 1 - i
            y1, y2 = i, n - 1 - i
            rc = []
            for x in range(x1, x2 + 1):
                rc.append(grid[x][y1])
            for y in range(y1+1, y2 + 1):
                rc.append(grid[x2][y])
            for x in range(x2-1, x1 - 1, -1):
                rc.append(grid[x][y2])
            for y in range(y2-1, y1, -1):
                rc.append(grid[x1][y])

            t = k % len(rc)
            last = rc[-t:]
            rc = rc[:-t]
            rc = last + rc

            j = 0
            for x in range(x1, x2 + 1):
                grid[x][y1] = rc[j]
                j += 1
            for y in range(y1+1, y2 + 1):
                grid[x2][y] = rc[j]
                j += 1
            for x in range(x2-1, x1 - 1, -1):
                grid[x][y2] = rc[j]
                j += 1
            for y in range(y2-1, y1, -1):
                grid[x1][y] = rc[j]
                j += 1
        return grid