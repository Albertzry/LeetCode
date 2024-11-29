class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        dis = [[float('inf')] * n for _ in range(m)]
        dis[0][0] = 0
        que = [[0, 0, 0]]
        while True:
            cost, i, j = heapq.heappop(que)
            if cost > dis[i][j]:
                continue
            if i == m - 1 and j == n - 1:
                return cost
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n :
                    nd = max(cost + 1, grid[x][y])
                    nd += (nd - x - y) % 2
                    if nd < dis[x][y]:
                        dis[x][y] = nd
                        heapq.heappush(que, [nd, x, y])