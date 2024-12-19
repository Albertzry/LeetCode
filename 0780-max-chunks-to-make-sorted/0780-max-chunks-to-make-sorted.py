class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = mx = 0
        for i, x in enumerate(arr):
            mx = max(mx, x)
            ans += mx == i
        return ans
