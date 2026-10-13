class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = list(map(lambda x: abs(x),nums))
        nums.sort(reverse=True)
        n = len(nums)
        ans = 0
        l,r = 0,n-1
        while l<r:
            ans += nums[l]**2 -nums[r]**2
            l+=1
            r-=1
        if l==r:
            ans+=nums[l]**2
        return ans
