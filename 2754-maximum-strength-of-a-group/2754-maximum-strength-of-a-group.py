class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        result = 1
        i,n,c=0,len(nums),0
        if len(nums)==1:
            return nums[0]
        while i<n:
            if i<n-1 and nums[i]<0 and nums[i+1]<0:
                result*=nums[i]
                result*=nums[i+1]
                c+=2
                i+=2
            elif nums[i]>0:
                result*=nums[i]
                c+=1
                i+=1
            else:i+=1
        if result==1 and c==0:
            return 0
        return result
