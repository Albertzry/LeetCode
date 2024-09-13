class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        res, n, runningCostSum = 0, len(chargeTimes), 0
        q, j = deque(), 0
        for i in range(n):
            runningCostSum += runningCosts[i]
            while q and chargeTimes[q[-1]] <= chargeTimes[i]:
                q.pop()
            q.append(i)
            while j <= i and (i - j + 1) * runningCostSum + chargeTimes[q[0]] > budget:
                if q and q[0] == j:
                    q.popleft()
                runningCostSum -= runningCosts[j]
                j += 1
            res = max(res, i - j + 1)
        return res
