class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mx,mn = [-1]*n,[-1]*n
        l,r=0,10**10
        for i in range(n):
            l=max(l,nums[i])
            mx[i] = l
            r=min(r,nums[n-1-i])
            mn[n-1-i]=r

        for i in range(n):
            if mx[i]-mn[i]<=k:
                return i
        
        return -1