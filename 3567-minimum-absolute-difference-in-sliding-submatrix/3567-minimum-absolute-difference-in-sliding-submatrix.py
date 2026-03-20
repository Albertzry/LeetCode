class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n-k+1)]for _ in range(m-k+1)]
        for i in range(m-k+1):
            for j in range(n-k+1):
                temp = []
                for p in range(k):
                    for q in range(k):
                        temp.append(grid[i+p][j+q])
                temp.sort()
                diff = temp[-1] - temp[0]
                for r in range(k**2 -1):
                    diff = min(diff,abs(temp[r+1]-temp[r])) if temp[r+1] - temp[r] != 0 else diff
                ans[i][j] = diff
        return ans