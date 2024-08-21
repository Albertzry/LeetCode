class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        for i in range(len(nums)):
            if abs(nums[i]) >= 0 and abs(nums[i]) <= len(nums):
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
