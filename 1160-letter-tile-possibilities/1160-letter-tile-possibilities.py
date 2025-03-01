class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        tile = set(tiles)

        def dfs(i):
            if i == 0:
                return 1
            res = 1
            for t in tile:
                if count[t] > 0:
                    count[t] -= 1
                    res += dfs(i - 1)
                    count[t] += 1
            return res

        return dfs(len(tiles)) - 1
