class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter([nums[i] * nums[j] for i in range(n) for j in range(i + 1, n)])
        ans = 0
        for _, v in cnt.items():
            ans += v * (v - 1) * 4
        return ans
