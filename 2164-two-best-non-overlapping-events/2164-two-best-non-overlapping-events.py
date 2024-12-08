class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        queue = []
        ans = 0
        max_value = 0
        for start, end, value in events:
            while queue and queue[0][0] < start:
                cur = heapq.heappop(queue)
                max_value = max(max_value, cur[1])

            ans = max(ans, max_value + value)

            heapq.heappush(queue, (end, value))

        return ans
