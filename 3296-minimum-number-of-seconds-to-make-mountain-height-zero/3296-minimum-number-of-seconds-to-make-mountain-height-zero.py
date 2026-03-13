class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        pq = []
        ans = 0
        for worker in workerTimes:
            heapq.heappush(pq,[worker,worker,1])

        while pq and mountainHeight > 0:
            mountainHeight -= 1
            worker = heapq.heappop(pq)
            ans = max(ans,worker[0])
            worker[2] += 1
            worker[0] += worker[1]*worker[2]
            heapq.heappush(pq,worker)
            
        return ans
        
