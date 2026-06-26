class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 表示前缀和为 -n, -(n-1), ..., 0, 1, ..., n 的前缀数量，下标偏移 n
        pre = [0] * (n * 2 + 1)
        pre[n] = 1
        cnt = n
        ans = presum = 0
        for i in range(n):
            if nums[i] == target:
                presum += pre[cnt]
                cnt += 1
                pre[cnt] += 1
            else:
                cnt -= 1
                presum -= pre[cnt]
                pre[cnt] += 1
            ans += presum
        return ans
