class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        if 2*nums[0]>nums[-1]:
            return 0
        left,right,res = 0,(n+1)//2,0
        while right<n:
            if 2*nums[left]<=nums[right]:
                res+=2
                left+=1
            right+=1
        return res
        
        