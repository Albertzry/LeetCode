class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack, ans = [], 0
        for i, x in enumerate(nums):
            if not stack or nums[stack[-1]] > x:
                stack.append(i)
        j = len(nums) - 1
        while stack and j >= 0:
            while j >= 0 and nums[j] < nums[stack[-1]]:
                j -= 1
            if j >= 0:
                ans = max(ans, j - stack.pop())
        return ans
