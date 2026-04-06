class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y = 0,0
        dir = 1
        ans = 0
        rc_x = defaultdict(list)
        rc_y = defaultdict(list)
        for ob in obstacles:
            rc_x[ob[0]].append(ob[1])
            rc_y[ob[1]].append(ob[0])
        for c in commands:
            if c == -1 :
                dir+=1
                continue
            elif c == -2 :
                dir-=1
                continue
            if dir%4 == 1:
                new_y = y+c
                for ob in rc_x[x]:
                    if y<ob and y+c>=ob:
                        new_y = min(new_y,ob-1)
                y = new_y
            elif dir%4 == 2:
                new_x = x+c
                for ob in rc_y[y]:
                    if x<ob and x+c>=ob:
                        new_x = min(new_x, ob-1)
                x = new_x
            elif dir%4 == 3:
                new_y = y-c
                for ob in rc_x[x]:
                    if y>ob and y-c<=ob:
                        new_y=max(new_y,ob+1)
                y = new_y
            elif dir%4 == 0:
                new_x = x-c
                for ob in rc_y[y]:
                    if x>ob and x-c<=ob:
                        new_x=max(new_x,ob+1)
                x = new_x
            ans = max(ans, x**2+y**2)
        return ans