class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j<len(grid[0])-1 and grid[i][j]==grid[i][j+1]:
                    return False
                if i<len(grid)-1 and grid[i][j]!=grid[i+1][j]:
                    return False
        return True