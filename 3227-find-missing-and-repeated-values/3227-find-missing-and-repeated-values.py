class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        map = [0]*(n*n)
        for i in range(n):
            for j in range(n):
                map[grid[i][j]-1]+=1
        return[1+map.index(2),1+map.index(0)]