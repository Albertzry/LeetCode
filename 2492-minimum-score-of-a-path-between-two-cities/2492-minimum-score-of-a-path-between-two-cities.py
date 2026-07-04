class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rc = defaultdict(list)
        for road in roads:
            rc[road[0]].append(road[1:])
            rc[road[1]].append([road[0],road[2]])
        group = set()
        s = []
        que = [1]
        while que:
            now = que[0]
            group.add(now)
            que.pop(0)
            for next in rc[now]:
                if next[0] not in group:
                    que.append(next[0])
                    s.append(next[1])
        return min(s)