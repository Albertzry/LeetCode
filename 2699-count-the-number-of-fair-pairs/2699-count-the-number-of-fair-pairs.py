class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        import bisect
        ans = 0
        nums.sort()
        for j, x in enumerate(nums):
            r = bisect.bisect_right(nums, upper - x, 0, j)
            l = bisect.bisect_left(nums, lower - x, 0, j)
            ans += r - l
        return ans
