class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        num = k
        while True:
            if num not in nums:
                return num
            num+=k
            