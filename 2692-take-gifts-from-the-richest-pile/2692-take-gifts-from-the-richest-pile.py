class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        gifts=list(map(lambda x:x*-1,gifts))
        gifts.sort()
        ans=0
        i=0
        while i<k:
            temp=heapq.heappop(gifts)
            heapq.heappush(gifts,-int(pow(-temp,0.5)))
            i+=1
        return -sum(gifts)