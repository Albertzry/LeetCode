class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target >= nums[0]:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                if nums[i] < nums[0]:
                    break
            return -1
        elif target <= nums[-1]:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == target:
                    return i
                if nums[i] > nums[-1]:
                    break
            return -1
        else: return -1