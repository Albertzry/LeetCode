class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        mi, ma = nums[0], nums[-1]
        res = ma - mi
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i+1]
            res = min(res, max(ma - k, a + k) - min(mi + k, b - k))
        return res

