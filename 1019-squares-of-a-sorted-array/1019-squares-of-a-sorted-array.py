class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=map(lambda x:x**2,nums)
        return sorted(nums)