class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prizePositions)
        dp = [0] * (n + 1)
        ans, left = 0, 0
        for right, x in enumerate(prizePositions):
            while x - prizePositions[left] > k:
                left += 1
            ans = max(ans, right - left + 1 + dp[left])
            dp[right + 1] = max(dp[right], right - left + 1)

        return ans
