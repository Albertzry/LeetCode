class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return len(set(nums[:])) == len(nums)-1 and nums.count(len(nums)-1) == 2 and sum(nums)== int(len(nums)*(len(nums)-1)/2 + len(nums)-1)