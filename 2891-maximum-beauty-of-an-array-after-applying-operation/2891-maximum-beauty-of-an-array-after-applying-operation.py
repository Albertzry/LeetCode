class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = left = 0
        for right, x in enumerate(nums):
            while x - nums[left] > k * 2:
                left += 1
            ans = max(ans, right - left + 1)
        return ans
