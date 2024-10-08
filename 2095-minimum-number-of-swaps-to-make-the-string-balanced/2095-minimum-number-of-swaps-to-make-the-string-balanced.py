class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = mincnt = 0
        for ch in s:
            if ch == '[':
                cnt += 1
            else:
                cnt -= 1
                mincnt = min(mincnt, cnt)
        return (-mincnt + 1) // 2
