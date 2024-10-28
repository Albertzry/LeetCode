class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(sorted(nums))
        ans = -1
        ceil = pow(max(nums),0.5)
        for num in nums:
            if num>ceil:
                continue
            temp = num
            res = 1
            while temp **2 in nums:
                res+=1
                temp **= 2
            if res!=1:
                ans = max(ans, res)
        return ans