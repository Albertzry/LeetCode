class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        for i in range(2):
            for j in range(2):
                sum=0
                if grid[i][j]=="B":
                    sum+=1
                if grid[i][j+1]=="B":
                    sum+=1
                if grid[i+1][j]=="B":
                    sum+=1
                if grid[i+1][j+1]=="B":
                    sum+=1
                if sum!=2:
                    return True
        return False 