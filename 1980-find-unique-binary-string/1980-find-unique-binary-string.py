class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        m = len(nums)
        max = 2**n -1
        nums.sort()
        for i in range(max+1):
            if i>=m or int(nums[i],2) != i:
                return format(i, '0%db' % n)
