class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        Col = len(grid[0])
        presum1 = [0 for _ in range(Col + 1)]
        for c in range(Col):
            presum1[c+1] = presum1[c] + grid[0][c]
        presum2 = [0 for _ in range(Col + 1)]
        for c in range(Col):
            presum2[c+1] = presum2[c] + grid[1][c]
        
        res = float('inf')
        for mid in range(Col):
            up = presum1[Col] - presum1[mid + 1]
            down = presum2[mid]
            res = min(res, max(up, down))
        return res
