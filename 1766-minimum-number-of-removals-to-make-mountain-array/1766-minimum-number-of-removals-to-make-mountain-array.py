class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        g = []
        for i in range(n - 1, 0, -1):
            x = nums[i]
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            suf[i] = j + 1  # 从 nums[i] 开始的最长严格递减子序列的长度

        mx = 0  # 最长山形子序列的长度
        g = []
        for i, x in enumerate(nums):
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            pre = j + 1  # 在 nums[i] 结束的最长严格递增子序列的长度
            if pre >= 2 and suf[i] >= 2:
                mx = max(mx, pre + suf[i] - 1)  # 减去重复的 nums[i]
        return n - mx
