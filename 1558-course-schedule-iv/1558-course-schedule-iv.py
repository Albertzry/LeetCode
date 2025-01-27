class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses
        isPre = [[False] * numCourses for _ in range(numCourses)]
        for p in prerequisites:
            indgree[p[1]] += 1
            g[p[0]].append(p[1])

        q = []
        for i in range(numCourses):
            if indgree[i] == 0:
                q.append(i)
        while len(q) > 0:
            cur = q[0]
            q.pop(0)
            for ne in g[cur]:
                isPre[cur][ne] = True
                for i in range(numCourses):
                    isPre[i][ne] = isPre[i][ne] or isPre[i][cur]
                indgree[ne] -= 1
                if indgree[ne] == 0:
                    q.append(ne)
        res = []
        for query in queries:
            res.append(isPre[query[0]][query[1]])
        return res
