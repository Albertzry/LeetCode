class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s: str, pos: int, tot: int, target: int) -> bool:
            if pos == len(s):
                return tot == target
            sum = 0
            for i in range(pos, len(s)):
                sum = sum * 10 + int(s[i])
                if sum + tot > target:
                    break
                if dfs(s, i + 1, sum + tot, target):
                    return True
            return False
        res = 0
        for i in range(1, n + 1):
            if dfs(str(i * i), 0, 0, i):
                res += i * i
        return res

