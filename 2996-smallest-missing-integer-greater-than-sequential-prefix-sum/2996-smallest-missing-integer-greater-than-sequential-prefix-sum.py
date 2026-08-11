class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i]!= nums[i-1]+1:
                break
            s+=nums[i]
        nums = set(nums)
        while True:
            if s not in nums:
                return s
            s+=1