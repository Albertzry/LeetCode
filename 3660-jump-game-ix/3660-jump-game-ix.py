class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        ans = [0] * n
        suf_min = inf
        for i in range(n - 1, -1, -1):
            ans[i] = pre_max[i] if pre_max[i] <= suf_min else ans[i + 1]
            suf_min = min(suf_min, nums[i])
        return ans
