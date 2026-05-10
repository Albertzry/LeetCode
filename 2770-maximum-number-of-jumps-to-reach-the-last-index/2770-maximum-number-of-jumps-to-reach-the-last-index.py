class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1]*n
        dp[0] = 0
        for i in range(n):
            for j in range(i):
                if abs(nums[i]-nums[j])<=target and dp[j]!=-1:
                    dp[i] = max(dp[j]+1,dp[i])
        return dp[-1]