class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = float('inf')
        for l in range(len(nums) - 2):
            if l>0 and nums[l]==nums[l-1]:
                continue
            m = l + 1
            r = len(nums) - 1
            while m < r:
                sum = nums[l] + nums[m] + nums[r]
                if sum == target:
                    return target
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum>target:
                    r-=1
                else:
                    m+=1
        return result