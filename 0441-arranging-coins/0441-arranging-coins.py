class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        while n>=0:
            res+=1
            n-=res
        return res-1