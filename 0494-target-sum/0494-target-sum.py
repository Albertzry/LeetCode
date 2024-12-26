class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0
        m = s // 2

        f = [1] + [0] * m
        for x in nums:
            for c in range(m, x - 1, -1):
                f[c] += f[c - x]
        return f[m]
