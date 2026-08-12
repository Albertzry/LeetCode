class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        rc = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(nums)):
            rc[nums[r]] += 1

            while rc[nums[r]] > k:
                rc[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans