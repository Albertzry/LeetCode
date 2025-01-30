class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)

        time = [0] * n  
        clock = 0
        def bfs(start: int) -> int:  
            depth = 0
            nonlocal clock
            clock += 1
            time[start] = clock
            q = [start]
            while q:
                tmp = q
                q = []
                for x in tmp:
                    for y in g[x]:
                        if time[y] != clock:  
                            time[y] = clock
                            q.append(y)
                depth += 1
            return depth

        color = [0] * n
        def is_bipartite(x: int, c: int) -> bool:  
            nodes.append(x)
            color[x] = c
            for y in g[x]:
                if color[y] == c or color[y] == 0 and not is_bipartite(y, -c):
                    return False
            return True

        ans = 0
        for i, c in enumerate(color):
            if c: continue
            nodes = []
            if not is_bipartite(i, 1): return -1  
            ans += max(bfs(x) for x in nodes)  
        return ans
