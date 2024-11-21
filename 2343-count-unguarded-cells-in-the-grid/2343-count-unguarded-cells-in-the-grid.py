class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0 for _ in range(n)]for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]]=1
        for wall in walls:
            grid[wall[0]][wall[1]]=2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if i!=m-1:
                        p=1
                        while i+p<m:
                            if grid[i+p][j]==1 or grid[i+p][j]==2:
                                break
                            grid[i+p][j]=-1
                            p+=1
                    if i!=0:
                        p=-1
                        while i+p>-1:
                            if grid[i+p][j]==1 or grid[i+p][j]==2:
                                break
                            grid[i+p][j]=-1
                            p-=1
                    if j!=n-1:
                        q=1
                        while j+q<n:
                            if grid[i][j+q]==1 or grid[i][j+q]==2:
                                break
                            grid[i][j+q]=-1
                            q+=1
                    if j!=0:
                        q=-1
                        while j+q>-1:
                            if grid[i][j+q]==1 or grid[i][j+q]==2:
                                break
                            grid[i][j+q]=-1
                            q-=1
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    ans+=1
        return ans
