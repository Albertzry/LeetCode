class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result, temp = 0, []
        if nums[0]>0:
            result += 1
        for i in range(len(nums)-1):
            temp.append(nums[i])
            if len(temp) > nums[i] and len(temp)<nums[i+1]:
                result += 1
        temp.append(nums[-1])
        if len(temp) > nums[-1]:
            result += 1
        return result
