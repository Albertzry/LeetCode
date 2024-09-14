class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = max(nums)
        l,r,res=0,0,0
        while l <len(nums):
            if nums[l]==target:
                r=l
                while r<len(nums) and nums[r]==target:
                    r+=1
                res=max(res,r-l)
                l=r-1
            l+=1
        return res
