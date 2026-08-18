class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        ans = -1
        if k == 1:
            for num in nums:
                if nums.count(num)!=1:
                    continue
                ans = max(ans,num)
        elif k == len(nums):
            ans = max(nums)
        else:
            if nums.count(nums[0]) == 1:
                ans = max(ans,nums[0])
            if nums.count(nums[-1]) == 1:
                ans = max(ans,nums[-1])
        return ans