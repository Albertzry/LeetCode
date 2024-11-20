class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        ans = 0
        cnt =Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for in_, out in zip(nums[k - 1:], nums):
            cnt[in_] += 1
            s += in_
            if len(cnt) == k:
                ans = max(ans, s)
            cnt[out] -= 1 
            if cnt[out] == 0:
                del cnt[out] 
            s -= out
        return ans