class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k
        dp = [0] *  k # 初始状态，表示尚未处理任何元素，因此不存在非空子数组
        
        for i in range(n):
            ndp = [0] * k # 当前层状态（滚动数组）

            ndp[nums[i] % k] += 1

            for r in range(k):
                ndp[(r * nums[i]) % k] += dp[r]

            dp = ndp # 更新状态

            # 累加答案
            for r in range(k):
                result[r] += dp[r] 
        return result
