class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def getCnt(prefix, n):
            cnt, cur, next = 0, prefix, prefix + 1
            while cur <= n:
                cnt += min(next, n + 1) - cur
                cur, next = cur * 10, next * 10
            return cnt

        poi, prefix = 1, 1
        while poi < k:
            cnt = getCnt(prefix, n)
            if poi + cnt > k:
                prefix *= 10
                poi += 1
            else:
                prefix += 1
                poi += cnt
        return prefix
