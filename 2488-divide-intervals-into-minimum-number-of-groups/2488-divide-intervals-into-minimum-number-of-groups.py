class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        import heapq
        intervals.sort()
        minHeap = []

        for l, r in intervals:
            if len(minHeap) == 0:
                heapq.heappush(minHeap, r)
            elif minHeap[0] < l:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, r)
            else:
                heapq.heappush(minHeap, r)

        res = len(minHeap)
        return res
