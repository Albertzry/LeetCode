class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        map = defaultdict(list)
        for time in times:
            map[time[0]].append(time[1:])
        dis = [float('inf')] * (n + 1)
        dis[0],dis[k] = 0,0
        que = [k]
        while que:
            node = que.pop(0)
            for next, cost in map[node]:
                if dis[next] > dis[node] + cost:
                    dis[next] = dis[node] + cost
                    que.append(next)
        return max(dis) if max(dis) != float('inf') else -1
        