class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum,left,ans=0,0,0
        for right in range(len(nums)):
            sum+= nums[right]==0
            while sum>k:
                sum-= nums[left]==0
                left+=1
            ans = max(ans,right-left+1)
        return ans