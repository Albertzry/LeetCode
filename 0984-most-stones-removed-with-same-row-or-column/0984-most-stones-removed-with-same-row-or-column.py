class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        row = defaultdict(list)
        column = defaultdict(list)
        for stone in stones:
            row[stone[0]].append(tuple(stone))
            column[stone[1]].append(tuple(stone))

        def dfs(i, j):
            for m in range(len(row[i])):
                if row[i][m] not in visited:
                    visited.append(row[i][m])
                    dfs(row[i][m][0], row[i][m][1])
            for n in range(len(column[j])):
                if column[j][n] not in visited:
                    visited.append(column[j][n])
                    dfs(column[j][n][0], column[j][n][1])

        visited = []
        num = 0
        for stone in stones:
            if tuple(stone) not in visited:
                dfs(stone[0], stone[1])
                num += 1
        return len(stones) - num



