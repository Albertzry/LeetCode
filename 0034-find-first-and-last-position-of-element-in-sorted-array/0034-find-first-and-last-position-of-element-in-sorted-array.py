class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums.count(target) == 0:
            return [-1, -1]

        def expand(i):
            l = i
            r = i
            while (l >= 0 and nums[l] == target) or (r < len(nums) and nums[r] == target):
                if l >= 0 and nums[l] == target:
                    l -= 1
                if r < len(nums) and nums[r] == target:
                    r += 1
            return [l + 1, r - 1]

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return expand(m)
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return [-1, -1]