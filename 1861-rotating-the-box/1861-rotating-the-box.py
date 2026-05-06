class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m,n = len(boxGrid), len(boxGrid[0])
        ans = [['.' for _ in range(m)] for _ in range(n)]
        stone = defaultdict(int)
        stone_pos = defaultdict(list)

        for i in range(m):
            rc = 0
            for j in range(n):
                if boxGrid[i][j] == '#':
                    rc+=1
                elif boxGrid[i][j] == '*':
                    stone[(i,j)] = rc
                    rc = 0
                    stone_pos[i].append(j)
            if rc != 0:
                stone[(i,-1)] = rc
                stone_pos[i].append(-1)
        
        for i in range(m):
            new_x = m-1-i
            for new_y in stone_pos[i]:
                stone_num = stone[(i,new_y)]
                if new_y == -1:
                    while stone_num >0:
                        ans[n-stone_num][new_x] = '#'
                        stone_num-=1
                    continue
                ans[new_y][new_x] = '*'
                while stone_num >0:
                    ans[new_y-stone_num][new_x] = '#'
                    stone_num-=1
        
        return ans
