class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        n=len(nums)
        while nums[0]>0:
            cnt=[0]*10
            for i in range(n):
                cnt[nums[i]%10]+=1
                nums[i]//=10
            for i in range(10):
                result+=(n-cnt[i])*cnt[i]
        return result/2