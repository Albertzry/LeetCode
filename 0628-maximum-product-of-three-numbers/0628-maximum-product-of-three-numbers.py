class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans1, ans2 = 0,0
        ans1 = nums[0]*nums[1]*nums[-1]
        ans2 = nums[-1]*nums[-2]*nums[-3]
        return max(ans1,ans2)