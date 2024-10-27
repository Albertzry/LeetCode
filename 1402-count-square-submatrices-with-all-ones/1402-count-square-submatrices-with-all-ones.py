class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp,nums=matrix,0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    if i>=1 and j>=1:
                        dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    nums+=dp[i][j]
        return nums
