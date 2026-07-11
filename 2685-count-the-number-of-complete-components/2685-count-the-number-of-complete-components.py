class Solution:
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                V = 0
                E = 0
                while stack:
                    u = stack.pop()
                    V += 1
                    E += len(graph[u])
                    for v in graph[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                if E == V * (V - 1):
                    ans += 1

        return ans
