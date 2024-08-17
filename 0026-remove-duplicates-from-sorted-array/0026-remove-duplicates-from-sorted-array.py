class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=set()
        r=0
        for i in range(len(nums)):
            if nums[i] not in result:
                result.add(nums[i])
                nums[r]=nums[i]
                r+=1
        return r