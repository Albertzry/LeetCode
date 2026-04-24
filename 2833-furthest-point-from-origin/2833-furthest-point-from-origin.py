class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = 0
        dis = 0
        for move in moves:
            if move == 'L':
                dis-=1
            elif move =='R':
                dis+=1
            elif move =='_':
                cnt+=1
        return abs(dis)+abs(cnt)