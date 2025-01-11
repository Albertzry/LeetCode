class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        right = len(s)
        occ = collections.Counter(s)
        left = sum(1 for _, v in occ.items() if v % 2 == 1)
        left = max(left, 1)
        return left <= k <= right