class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        cnt=[0]*n
        for edge in edges:
            cnt[edge[1]]+=1
        if cnt.count(0)>1:
            return -1
        else:
            return cnt.index(0)