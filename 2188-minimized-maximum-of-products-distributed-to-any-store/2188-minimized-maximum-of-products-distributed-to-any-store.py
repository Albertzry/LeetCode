class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        def check(x):
            cnt = 0
            for q in quantities:
                cnt += (q - 1) // x + 1
            return cnt <= n
        l, r = 1, max(quantities) + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
