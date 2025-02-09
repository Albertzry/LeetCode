class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, cnt = len(nums), Counter()
        ans = n * (n - 1) // 2
        for i, num in enumerate(nums):
            ans -= cnt[num - i]  
            cnt[num - i] += 1
        return ans
