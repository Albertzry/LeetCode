class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        rec = [[0] * 11 for _ in range(n)]
        for p,c in pick:
            rec[p][c]+=1
        ans=0
        for i in range(n):
            if max(rec[i])>i:
                ans+=1
        return ans
            