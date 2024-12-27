class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        ans = 0
        mx = values[0] + 0
        for j in range(1, len(values)):
            ans = max(ans, mx + values[j] - j)
            mx = max(mx, values[j] + j)
        return ans
