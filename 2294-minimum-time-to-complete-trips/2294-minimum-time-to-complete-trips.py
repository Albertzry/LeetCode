class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        def check(t):
            cnt = 0
            for period in time:
                cnt += t // period
            return cnt >= totalTrips
        
        l = 1
        r = totalTrips * max(time)

        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l