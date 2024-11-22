class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cnt = Counter()
        for row in matrix:
            if row[0]: 
                for j in range(len(row)):
                    row[j] ^= 1
            cnt[tuple(row)] += 1
        return max(cnt.values())
