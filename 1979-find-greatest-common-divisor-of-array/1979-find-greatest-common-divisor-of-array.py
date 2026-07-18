class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        b = max(nums)
        for i in range(s,0,-1):
            if s%i==0 and b%i == 0:
                return i