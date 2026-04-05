class Solution:
    def judgeCircle(self, moves: str) -> bool:
         cnt_l, cnt_r, cnt_u, cnt_d = moves.count('L'),moves.count('R'),moves.count('U'),moves.count('D')
         return cnt_l == cnt_r and cnt_u == cnt_d