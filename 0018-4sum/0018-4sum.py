class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(len(nums) - 1, 0, -1):
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    continue
                l = i + 1
                r = j-1
                while l < r:
                    if target == nums[i] + nums[l] + nums[r] + nums[j]:
                        if [nums[i], nums[l], nums[r], nums[j]] not in result:
                            result.append([nums[i], nums[l], nums[r], nums[j]])
                        l += 1
                        r -= 1
                    elif target > nums[i] + nums[l] + nums[r] + nums[j]:
                        l += 1
                    else:
                        r -= 1
        return result