class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        f = 0
        for i,num in enumerate(nums):
            f += i*num
        ans = f
        for i in range(1,n):
            f = f + num_sum - n*nums[n-i]
            ans = max(ans,f)
        return ans
