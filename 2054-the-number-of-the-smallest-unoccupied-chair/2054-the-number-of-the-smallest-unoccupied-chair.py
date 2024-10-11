class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        from heapq import heappop,heappush
        start,end=[],[]
        n=len(times)
        for i , time in enumerate(times):
            start.append((time[0],i))
            end.append((time[1],i))
        chair = [i for i in range(n)]
        seats=dict()
        start.sort()
        end.sort()
        j = 0
        for time,i in start:
            while j<n and end[j][0]<=time:
                heappush(chair,seats[end[j][1]])
                j+=1
            seats[i]=heappop(chair)
            if i == targetFriend:
                return seats[i]
        return -1



        