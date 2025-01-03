class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        temp=[0]*(n+1)
        for i in range(n):
            temp[i+1]=temp[i]+nums[i]
        ans=0
        for i in range(1,n):
            if temp[i]-temp[0]>=temp[n]-temp[i]:
                ans+=1
        return ans