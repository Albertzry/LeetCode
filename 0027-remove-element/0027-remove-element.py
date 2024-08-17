class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)-nums.count(val)
        for i in range(nums.count(val)):
            nums.remove(val)
        return k