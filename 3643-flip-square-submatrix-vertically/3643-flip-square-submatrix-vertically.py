class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        temp = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                temp[i][j] = grid[x+i][y+j]
        
        for i in range(k):
            for j in range(k):
                grid[x+k-1-i][y+j] = temp[i][j]
        
        return grid