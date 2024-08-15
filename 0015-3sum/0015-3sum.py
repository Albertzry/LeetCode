class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for l in range(len(nums)):
            if nums[l]>0:
                break
            if l>0 and nums[l]==nums[l-1]:
                continue
            m = l + 1
            r = len(nums) - 1
            while m < r:
                sum = nums[l] + nums[m] + nums[r]
                if sum == 0:
                    if [nums[l], nums[m], nums[r]] not in result:
                        result.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    m += 1
        return result