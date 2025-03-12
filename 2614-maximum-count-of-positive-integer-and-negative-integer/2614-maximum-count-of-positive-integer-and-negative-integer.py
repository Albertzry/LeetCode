class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        m=int((l+r)/2)
        while m!=0 and m!=(n-1):
            if nums[m]>0 and (nums[m-1]<=0):
                break
            if nums[m]<=0:
                l=m
                m=int((l+m)/2)+1
            else:
                r=m
                m=int((l+m)/2)
        if m==n-1:
            pos=0
        else:
            pos=n-m
        neg=0
        for i in range(m,-1,-1):
            if nums[i]<0:
                neg=i+1
                break
        return max(pos,neg)