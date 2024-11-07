class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        windows,ans=[],[]
        cnt=0
        for i in range(len(nums)):
            windows.append(nums[i])
            if i>0 and nums[i]-nums[i-1]!=1:
                cnt=k-1
            if len(windows)<k:
                cnt-=1
                continue
            if cnt>0:
                ans.append(-1)
                cnt-=1
            else :
                ans.append(windows[-1])
            windows.pop(0)
        return ans